# core/use_cases/usuario_use_cases.py
from typing import Optional
from core.models_domain.usuarios import Usuario
from core.repositories.usuario_repository import UsuarioRepository


class CrearUsuario:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self, usuario: Usuario) -> Usuario:
        return self.repository.guardar(usuario)


class ObtenerUsuarioPorId:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self, usuario_id: int) -> Optional[Usuario]:
        return self.repository.obtener_por_id(usuario_id)


class ObtenerUsuarioPorUsername:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self, username: str) -> Optional[Usuario]:
        return self.repository.obtener_por_username(username)


class EliminarUsuario:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def execute(self, usuario_id: int) -> None:
        self.repository.eliminar(usuario_id)
