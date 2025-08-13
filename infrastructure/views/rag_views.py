from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from core.use_cases.rag_case_uses import CrearRAG
from core.use_cases.rag_case_uses import ObtenerRAGPorId
from core.use_cases.rag_case_uses import ListarRAGsPorUsuario
from core.use_cases.rag_case_uses import EliminarRAG

from infrastructure.repositories.rag_repository_django import DjangoRAGRepository


@csrf_exempt
def crear_rag_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Solo se permite POST.")

    data = json.loads(request.body.decode("utf-8"))
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    privado = data.get("privado", False)
    usuario_id = data.get("usuario_id")

    use_case = CrearRAG(DjangoRAGRepository())
    rag = use_case.execute(nombre, descripcion, privado, usuario_id)

    return JsonResponse({
        "id": rag.id,
        "nombre": rag.nombre,
        "descripcion": rag.descripcion,
        "privado": rag.privado,
        "usuario_id": rag.usuario_id
    })


def obtener_rag_por_id_view(request, rag_id):
    use_case = ObtenerRAGPorId(DjangoRAGRepository())
    rag = use_case.execute(rag_id)

    if not rag:
        return HttpResponseNotFound("RAG no encontrado.")

    return JsonResponse({
        "id": rag.id,
        "nombre": rag.nombre,
        "descripcion": rag.descripcion,
        "privado": rag.privado,
        "usuario_id": rag.usuario_id
    })


def listar_rags_por_usuario_view(request, usuario_id):
    use_case = ListarRAGsPorUsuario(DjangoRAGRepository())
    rags = use_case.execute(usuario_id)

    return JsonResponse([
        {
            "id": rag.id,
            "nombre": rag.nombre,
            "descripcion": rag.descripcion,
            "privado": rag.privado,
            "usuario_id": rag.usuario_id
        } for rag in rags
    ], safe=False)


@csrf_exempt
def eliminar_rag_view(request, rag_id):
    if request.method != "DELETE":
        return HttpResponseBadRequest("Solo se permite DELETE.")

    use_case = EliminarRAG(DjangoRAGRepository())
    use_case.execute(rag_id)

    return JsonResponse({"mensaje": "RAG eliminado correctamente."})