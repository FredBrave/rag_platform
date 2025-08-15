from rest_framework.response import Response
from rest_framework.decorators import api_view
from infrastructure.serializers.conversacion_serializer import ConversacionSerializer
from infrastructure.repositories.conversacion_repository_django import ConversacionRepositoryDjango
from core.use_cases.conversacion_case_uses import CrearConversacion, ListarConversacionesPorUsuario, ObtenerConversacionPorId, EliminarConversacion
from rest_framework import status

@api_view(['POST'])
def CrearConversacionView(request):
    data = request.data
    caso_uso = CrearConversacion(ConversacionRepositoryDjango())
    conversacion = caso_uso.execute(
        rag_id=data.get("rag_id"),
        usuario_id=data.get("usuario_id"),
        titulo=data.get("titulo")
        )
    serializer = ConversacionSerializer(conversacion)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def ObtenerConversacionView(request, conversacion_id):
    caso_uso = ObtenerConversacionPorId(ConversacionRepositoryDjango())
    conversacion = caso_uso.execute(conversacion_id)

    if not conversacion:
        return Response({"detail": "Conversación no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ConversacionSerializer(conversacion)
    return Response(serializer.data)

@api_view(['GET'])
def ListarConversacionesUsuarioView(requets, usuario_id):
        caso_uso = ListarConversacionesPorUsuario(ConversacionRepositoryDjango())
        conversaciones = caso_uso.execute(usuario_id)
        serializer = ConversacionSerializer(conversaciones, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def EliminarConversacionView(requets, conversacion_id):
        caso_uso = EliminarConversacion(ConversacionRepositoryDjango())
        caso_uso.execute(conversacion_id)
        return Response(status=status.HTTP_204_NO_CONTENT)