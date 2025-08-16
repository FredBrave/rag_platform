from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from infrastructure.serializers.api_key_serializer import APIKeySerializer
from infrastructure.repositories.api_key_repository_django import APIKeyRepositoryDjango
from core.use_cases.api_key_case_uses import (
    CrearAPIKey, ObtenerAPIKeyPorId,
    ListarAPIKeysPorUsuario, DesactivarAPIKey, EliminarAPIKey
)

@api_view(['POST'])
def CrearAPIKeyView(request, usuario_id):
    serializer = APIKeySerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        use_case = CrearAPIKey(APIKeyRepositoryDjango())
        api_key = use_case.execute(
            usuario_id=usuario_id,
            proveedor=data["proveedor"],
            clave=data["clave"],
        )
        return Response(APIKeySerializer(api_key).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ObtenerAPIKeyView(request, api_key_id, usuario_id):
        use_case = ObtenerAPIKeyPorId(APIKeyRepositoryDjango())
        api_key = use_case.execute(api_key_id)
        if api_key:
            return Response(APIKeySerializer(api_key).data)
        return Response({"error": "API Key no encontrada"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ListarAPIKeysUsuarioView(request, usuario_id):
        use_case = ListarAPIKeysPorUsuario(APIKeyRepositoryDjango())
        api_keys = use_case.execute(usuario_id)
        return Response(APIKeySerializer(api_keys, many=True).data)

@api_view(['PATCH'])
def DesactivarAPIKeyView(request, api_key_id, usuario_id):
        use_case = DesactivarAPIKey(APIKeyRepositoryDjango())
        api_key = use_case.execute(api_key_id)
        if api_key:
            return Response(APIKeySerializer(api_key).data)
        return Response({"error": "API Key no encontrada"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def EliminarAPIKeyView(request, api_key_id, usuario_id):
        use_case = EliminarAPIKey(APIKeyRepositoryDjango())
        api_key = use_case.execute(api_key_id)
        if api_key:
            return Response({"mensaje": "API Key eliminada lógicamente"})
        return Response({"error": "API Key no encontrada"}, status=status.HTTP_404_NOT_FOUND)