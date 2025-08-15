from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.use_cases.rag_case_uses import ObtenerRagPorId, CrearRAG, EliminarRAG, ListarRAGsPorUsuario
from core.use_cases.rag_permisos_case_uses import CrearPermisoRAG, ObtenerPermisosPorRAG, PuedeUsuarioEditarRAG, EliminarPermisoRAG
from infrastructure.repositories.rag_repository_django import RagRepositoryDjango
from infrastructure.repositories.rag_permisos_repository_django import RAGPermisoRepositoryDjango
from infrastructure.serializers.rag_serializer import RAGSerializer
from infrastructure.serializers.rag_permiso_serializer import RagPermisoSerializer
from rest_framework import status

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
    serializer = RAGSerializer(rag)
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


@api_view(['POST'])
def crear_permiso_rag_view(request, rag_id):
    data = request.data
    use_case = CrearPermisoRAG(RAGPermisoRepositoryDjango())
    rag_permiso = use_case.execute(
        rag_id=rag_id,
        usuario_id=data.get('usuario_id'),
        puede_editar=data.get('puede_editar')
    )
    serializer = RagPermisoSerializer(rag_permiso)
    return Response(serializer.data)

@api_view(['GET'])
def obtener_permisos_por_rag_view(request, rag_id):
    use_case = ObtenerPermisosPorRAG(RAGPermisoRepositoryDjango())
    rag_permisos = use_case.execute(rag_id)
    if rag_permisos is None:
        return Response({"error":"El Rag no existe"}, status=status.HTTP_404_NOT_FOUND)
    serializer = RagPermisoSerializer(rag_permisos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def puede_editar_rag_view(request, rag_id):
    #usuario_id = request.user.id
    use_case = PuedeUsuarioEditarRAG(RAGPermisoRepositoryDjango())
    puede_editar = use_case.execute(rag_id, 1)
    return Response({"puede_editar": puede_editar}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def eliminar_rag_permiso_view(request, rag_permiso_id):
    use_case = EliminarPermisoRAG(RAGPermisoRepositoryDjango())
    try:
        use_case.execute(rag_permiso_id)
        return Response({"message": "Rag permiso eliminado correctamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)