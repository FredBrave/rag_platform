from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.use_cases.usuario_case_uses import CrearUsuario, ObtenerUsuarioPorId, ObtenerUsuarioPorUsername, EliminarUsuario
from infrastructure.repositories.usuario_repository_django import UsuarioRepositoryDjango
from infrastructure.serializers.usuario_serializer import UsuarioSerializer

@api_view(['POST'])
def CrearUsuarioView(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        usuario_data = serializer.validated_data
        use_case = CrearUsuario(UsuarioRepositoryDjango())
        usuario = use_case.execute(usuario_data)
        return Response(UsuarioSerializer(usuario).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ObtenerUsuarioPorIdView(request, usuario_id):
    use_case = ObtenerUsuarioPorId(UsuarioRepositoryDjango())
    usuario = use_case.execute(usuario_id)
    if usuario:
        return Response(UsuarioSerializer(usuario).data, status=status.HTTP_200_OK)
    return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ObtenerUsuarioPorUsernameView(request, username):
    use_case = ObtenerUsuarioPorUsername(UsuarioRepositoryDjango())
    usuario = use_case.execute(username)
    if usuario:
        return Response(UsuarioSerializer(usuario).data, status=status.HTTP_200_OK)
    return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def EliminarUsuarioView(request, usuario_id):
        use_case = EliminarUsuario(UsuarioRepositoryDjango())
        use_case.execute(usuario_id)
        return Response({"detail": "Usuario eliminado"}, status=status.HTTP_204_NO_CONTENT)