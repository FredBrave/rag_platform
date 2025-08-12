from typing import List
from core.models_domain.conversaciones import Mensaje
from core.repositories.conversacion_repository import MensajeRepository


class CrearMensaje:
    def __init__(self, repository: MensajeRepository):
        self.repository = repository

    def execute(self, mensaje: Mensaje) -> Mensaje:
        return self.repository.guardar(mensaje)


class ListarMensajesPorConversacion:
    def __init__(self, repository: MensajeRepository):
        self.repository = repository

    def execute(self, conversacion_id: int) -> List[Mensaje]:
        return self.repository.listar_por_conversacion(conversacion_id)


class EliminarMensajesPorConversacion:
    def __init__(self, repository: MensajeRepository):
        self.repository = repository

    def execute(self, conversacion_id: int) -> None:
        self.repository.eliminar_por_conversacion(conversacion_id)
