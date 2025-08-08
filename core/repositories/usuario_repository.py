from abc import ABC, abstractmethod
from typing import Optional
from core.models_domain.usuarios import Usuario

class UsuarioRepository(ABC):

    @abstractmethod
    def guardar(self, usuario: Usuario) -> Usuario:
        """Guarda o actualiza un usuario y devuelve la entidad guardada."""
        pass

    @abstractmethod
    def obtener_por_id(self, usuario_id: int) -> Optional[Usuario]:
        """Obtiene un usuario por su ID."""
        pass

    @abstractmethod
    def obtener_por_username(self, username: str) -> Optional[Usuario]:
        """Obtiene un usuario por su nombre de usuario."""
        pass

    @abstractmethod
    def eliminar(self, usuario_id: int) -> None:
        """Elimina un usuario dado su ID."""
        pass