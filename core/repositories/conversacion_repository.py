from abc import ABC, abstractmethod
from typing import List, Optional
from core.models_domain.conversaciones import Conversacion, Mensaje

class ConversacionRepository(ABC):

    @abstractmethod
    def guardar(self, conversacion: Conversacion) -> Conversacion:
        """Guarda o actualiza una conversación y devuelve la entidad."""
        pass

    @abstractmethod
    def obtener_por_id(self, conversacion_id: int) -> Optional[Conversacion]:
        """Obtiene una conversación por su ID."""
        pass

    @abstractmethod
    def listar_por_usuario(self, usuario_id: int) -> List[Conversacion]:
        """Lista todas las conversaciones de un usuario."""
        pass

    @abstractmethod
    def eliminar(self, conversacion_id: int) -> None:
        """Elimina una conversación dado su ID."""
        pass


class MensajeRepository(ABC):

    @abstractmethod
    def guardar(self, mensaje: Mensaje) -> Mensaje:
        """Guarda un mensaje y devuelve la entidad guardada."""
        pass

    @abstractmethod
    def listar_por_conversacion(self, conversacion_id: int) -> List[Mensaje]:
        """Lista todos los mensajes asociados a una conversación."""
        pass

    @abstractmethod
    def eliminar_por_conversacion(self, conversacion_id: int) -> None:
        """Elimina todos los mensajes asociados a una conversación."""
        pass