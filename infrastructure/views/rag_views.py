from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from core.use_cases.rag_case_uses import CrearRAG, ObtenerRAGPorId, ListarRAGsPorUsuario, EliminarRAG

from infrastructure.repositories.rag_repository_django import RAGRepositoryDjango


@csrf_exempt
def crear_rag_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Solo se permite POST.")

    data = json.loads(request.body.decode("utf-8"))
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    privado = data.get("privado", False)
    usuario_id = data.get("usuario_id")

    use_case = CrearRAG(RAGRepositoryDjango())
    rag = use_case.execute(nombre, descripcion, privado, usuario_id)

    return JsonResponse({
        "id": rag.id,
        "nombre": rag.nombre,
        "descripcion": rag.descripcion,
        "privado": rag.privado,
        "usuario_id": rag.usuario_id
    })


def obtener_rag_por_id_view(request, rag_id):
    use_case = ObtenerRAGPorId(RAGRepositoryDjango())
    rag = use_case.execute(rag_id)

    if not rag:
        return HttpResponseNotFound("RAG no encontrado.")

    return JsonResponse({
        "id": rag.id,
        "nombre": rag.nombre,
        "descripcion": rag.descripcion,
        "privacidad": rag.privacidad,
        "usuario_id": rag.usuario_id
    })


def listar_rags_por_usuario_view(request, creador_id):
    use_case = ListarRAGsPorUsuario(RAGRepositoryDjango())
    rags = use_case.execute(creador_id)

    return JsonResponse([
        {
            "id": rag.id,
            "nombre": rag.nombre,
            "descripcion": rag.descripcion,
            "privacidad": rag.privacidad,
            "creador_id": rag.creador_id
        } for rag in rags
    ], safe=False)


@csrf_exempt
def eliminar_rag_view(request, rag_id):
    if request.method != "DELETE":
        return HttpResponseBadRequest("Solo se permite DELETE.")

    use_case = EliminarRAG(RAGRepositoryDjango())
    use_case.execute(rag_id)

    return JsonResponse({"mensaje": "RAG eliminado correctamente."})