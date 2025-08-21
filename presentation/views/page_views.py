from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from infrastructure.repositories.rag_repository_django import RagRepositoryDjango
from infrastructure.repositories.conversacion_repository_django import ConversacionRepositoryDjango
from infrastructure.repositories.documento_repository_django import DocumentoRepositoryDjango
from infrastructure.repositories.mensaje_repository_django import MensajeRepositoryDjango
from core.use_cases.rag_case_uses import ListarRAGsPorPrivacidad, ListarRAGsPorUsuario, CrearRAG, EditarRAG, EliminarRAG
from core.use_cases.conversacion_case_uses import ListarConversacionesPorUsuario, CrearConversacion, EliminarConversacion
from core.use_cases.documento_case_uses import ListarDocumentos, CrearDocumento, EliminarDocumento
from core.use_cases.mensaje_case_uses import CrearMensaje, ListarMensajesPorConversacion
from presentation.forms import RAGForm, DocumentoForm, ConversacionForm
from infrastructure.models.rag import RAG as RAGORM
from infrastructure.models.conversaciones import Conversacion as ConversacionORM


@login_required(login_url='login')
def home(request):
    listar_rags = ListarRAGsPorPrivacidad(RagRepositoryDjango())
    public_rags = listar_rags.execute(privacidad="publico")

    context = {
        'public_rags': public_rags,
    }
    return render(request, 'home.html', context)


@login_required
def mis_rags(request):
    listar_rags = ListarRAGsPorUsuario(RagRepositoryDjango())

    user_rags = listar_rags.execute(request.user.id)
    
    context = {
        "user_rags": user_rags
    }
    return render(request, "rags/mis_rags.html", context)


@login_required
def crear_rag(request):
    error_msg = None
    if request.method == "POST":
        form = RAGForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                crear_rag_use_case = CrearRAG(RagRepositoryDjango())
                crear_rag_use_case.execute(
                    nombre=data["nombre"],
                    descripcion=data["descripcion"],
                    privacidad=data["privacidad"] == "privado",
                    creador_id=request.user.id,
                    modelo_llm=data["modelo_llm"],
                    embedding_model=data["embedding_model"]
                )
                return redirect("mis_rags")
            except Exception as e:
                error_msg = f"Ocurrió un error al crear el RAG: {str(e)}"
    else:
        form = RAGForm()
    return render(request, "rags/crear_rag.html", {"form": form, "error_msg": error_msg})



@login_required
def editar_rag(request, rag_id):
    rag_repo = RagRepositoryDjango()
    rag = rag_repo.obtener_por_id(rag_id)
    if not rag or rag.creador_id != request.user.id:
        return redirect("mis_rags")

    if request.method == "POST":
        form = RAGForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                editar_rag_use_case = EditarRAG(rag_repo)
                editar_rag_use_case.execute(rag_id, data)
                return redirect("mis_rags")
            except Exception as e:
                form.add_error(None, f"Ocurrió un error al editar el RAG: {str(e)}")
    else:
        form = RAGForm(initial={
            "nombre": rag.nombre,
            "descripcion": rag.descripcion,
            "privacidad": rag.privacidad,
            "modelo_llm": rag.modelo_llm,
            "embedding_model": rag.embedding_model
        })

    return render(request, "rags/crear_rag.html", {"form": form, "rag": rag})



@login_required
def eliminar_rag(request, rag_id):
    try:
        rag_obj = RAGORM.objects.get(pk=rag_id)
        
        if rag_obj.creador_id != request.user.id:
            messages.error(request, "No tienes permiso para eliminar este RAG.")
            return redirect('mis_rags')
        
        eliminar_rag_use_case = EliminarRAG(RagRepositoryDjango())
        eliminar_rag_use_case.execute(rag_id)
        messages.success(request, "RAG eliminado correctamente.")
        return redirect('mis_rags')
    
    except RAGORM.DoesNotExist:
        messages.error(request, "El RAG que intentas eliminar no existe.")
        return redirect('mis_rags')
    except Exception as e:
        messages.error(request, f"Ocurrió un error al eliminar el RAG: {e}")
        return redirect('mis_rags')
    
@login_required
def detalle_rag(request, rag_id):
    rag = get_object_or_404(RAGORM, id=rag_id, creador=request.user)
    documento_repository = DocumentoRepositoryDjango()
    conversacion_repository = ConversacionRepositoryDjango()
    listar_documentos = ListarDocumentos(documento_repository)
    listar_conversaciones = ListarConversacionesPorUsuario(conversacion_repository)
    documentos = [doc for doc in listar_documentos.execute() if doc.rag_id == rag.id]
    conversaciones = [
        conv for conv in listar_conversaciones.execute(request.user.id) 
        if conv.rag_id == rag.id
    ]
    return render(request, "rags/detalle_rag.html", {
        "rag": rag,
        "documentos": documentos,
        "conversaciones": conversaciones
    })



@login_required
def crear_conversacion(request, rag_id):
    rag = get_object_or_404(RAGORM, id=rag_id, creador=request.user)
    conversacion_repository = ConversacionRepositoryDjango()
    crear_conversacion_uc = CrearConversacion(conversacion_repository)

    if request.method == "POST":
        form = ConversacionForm(request.POST)
        if form.is_valid():
            crear_conversacion_uc.execute(
                rag.id,
                request.user.id,
                form.cleaned_data['titulo']
            )
            return redirect("detalle_rag", rag_id=rag.id)
    else:
        form = ConversacionForm()

    return render(request, "rags/crear_conversacion.html", {
        "rag": rag,
        "form": form
    })

@login_required
def crear_documento(request, rag_id):
    rag = get_object_or_404(RAGORM, id=rag_id, creador=request.user)
    documento_repository = DocumentoRepositoryDjango()
    crear_documento_uc = CrearDocumento(documento_repository)

    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            crear_documento_uc.execute(
                rag.id,
                form.cleaned_data['nombre'],
                form.cleaned_data['archivo']
            )
            return redirect("detalle_rag", rag_id=rag.id)
    else:
        form = DocumentoForm()

    return render(request, "rags/crear_documento.html", {
        "rag": rag,
        "form": form
    })


@login_required
def detalle_conversacion(request, rag_id, conversacion_id):
    rag = get_object_or_404(RAGORM, id=rag_id)
    conversacion = get_object_or_404(ConversacionORM, id=conversacion_id, rag=rag)

    repo = MensajeRepositoryDjango()
    listar_mensajes = ListarMensajesPorConversacion(repo)
    crear_mensaje = CrearMensaje(repo)

    mensajes = listar_mensajes.execute(conversacion_id)

    if request.method == "POST":
        contenido = request.POST.get("contenido")
        if contenido:
            crear_mensaje.execute(conversacion_id, contenido, rol="usuario")
            return redirect("detalle_conversacion", rag_id=rag.id, conversacion_id=conversacion.id)

    return render(request, "rags/detalle_conversacion.html", {
        "rag": rag,
        "conversacion": conversacion,
        "mensajes": mensajes,
    })


@login_required
def eliminar_documento(request, rag_id, documento_id):
    rag = get_object_or_404(RAGORM, id=rag_id)

    if request.method == "POST":
        repo = DocumentoRepositoryDjango()
        eliminar_documento_uc = EliminarDocumento(repo)
        eliminar_documento_uc.execute(documento_id)

    return redirect("detalle_rag", rag_id=rag.id)


@login_required
def eliminar_conversacion(request, rag_id, conversacion_id):
    rag = get_object_or_404(RAGORM, id=rag_id)

    if request.method == "POST":
        repo = ConversacionRepositoryDjango()
        eliminar_conversacion_uc = EliminarConversacion(repo)
        eliminar_conversacion_uc.execute(conversacion_id)

    return redirect("detalle_rag", rag_id=rag.id)