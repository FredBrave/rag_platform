from abc import ABC, abstractmethod
from typing import List, Optional
from core.models_domain.api_keys import APIKey

class APIKeyRepository(ABC):

    @abstractmethod
    def guardar(self, api_key: APIKey) -> APIKey:
        """Guarda o actualiza una API Key y devuelve la entidad guardada."""
        pass

    @abstractmethod
    def obtener_por_id(self, api_key_id: int) -> Optional[APIKey]:
        """Obtiene una API Key por su ID."""
        pass

    @abstractmethod
    def listar_por_usuario(self, usuario_id: int) -> List[APIKey]:
        """Lista todas las API Keys de un usuario."""
        pass

    @abstractmethod
    def desactivar(self, api_key_id: int) -> None:
        """Desactiva una API Key (borrado lógico)."""
        pass

    @abstractmethod
    def eliminar(self, api_key_id: int) -> None:
        """Elimina físicamente una API Key."""
        pass