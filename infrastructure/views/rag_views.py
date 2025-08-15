from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.use_cases.rag_case_uses import ObtenerRagPorId, CrearRAG, EliminarRAG, ListarRAGsPorUsuario
from infrastructure.repositories.rag_repository_django import RagRepositoryDjango
from infrastructure.serializers.rag_serializer import RAGSerializer
from rest_framework import status
import json

@api_view(['POST'])
def crear_rag_view(request):
    data = request.data
    use_case = CrearRAG(RagRepositoryDjango())
    rag = use_case.execute(
        nombre=data.get("nombre"),
        descripcion=data.get("descripcion"),
        privacidad=data.get("privacidad"),
        creador_id=data.get("creador_id"),
        modelo_llm=data.get("modelo_llm", "gpt-4o"),
        embedding_model=data.get("embedding_model", "text-embedding-3-small")
    )
    serializer = RAGSerializer(rag.__dict__)
    return Response(serializer.data)
    


@api_view(['GET'])
def obtener_rag_por_id_view(request, rag_id):
    use_case = ObtenerRagPorId(RagRepositoryDjango())
    rag_obj = use_case.execute(rag_id)

    if rag_obj is None:
        return Response(
            {"error": "RAG no encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = RAGSerializer(rag_obj.__dict__)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def listar_rags_por_usuario_view(request, creador_id):
    use_case = ListarRAGsPorUsuario(RagRepositoryDjango())
    rags = use_case.execute(creador_id)
    if rags is None:
        return Response({"error":"Usuario no existe o no tiene ningun RAG"}, status=status.HTTP_404_NOT_FOUND)
    serializer = RAGSerializer(rags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def eliminar_rag_view(request, rag_id):
    use_case = EliminarRAG(RagRepositoryDjango())
    try:
        use_case.execute(rag_id)
        return Response({"message": "RAG eliminado correctamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
