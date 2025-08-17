from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from infrastructure.repositories.rag_repository_django import RagRepositoryDjango
from core.use_cases.rag_case_uses import ListarRAGsPorPrivacidad, ListarRAGsPorUsuario, CrearRAG, EditarRAG, EliminarRAG
from presentation.forms import RAGForm
from infrastructure.models.rag import RAG as RAGORM


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