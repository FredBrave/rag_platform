from typing import List, Optional
from core.models_domain.conversaciones import Conversacion
from core.repositories.conversacion_repository import ConversacionRepository
from datetime import datetime


class CrearConversacion:
    def __init__(self, conversacion_repository: ConversacionRepository):
        self.conversacion_repository = conversacion_repository

    def execute(self, rag_id: int, usuario_id: int, titulo: str) -> Conversacion:
        conversacion = Conversacion(
            id=None,
            rag_id=rag_id,
            usuario_id=usuario_id,
            titulo=titulo,
            fecha_creacion=datetime.now()
        )
        return self.conversacion_repository.guardar(conversacion)


class ObtenerConversacionPorId:
    def __init__(self, conversacion_repository: ConversacionRepository):
        self.conversacion_repository = conversacion_repository

    def execute(self, conversacion_id: int) -> Optional[Conversacion]:
        return self.conversacion_repository.obtener_por_id(conversacion_id)


class ListarConversacionesPorUsuario:
    def __init__(self, conversacion_repository: ConversacionRepository):
        self.conversacion_repository = conversacion_repository

    def execute(self, usuario_id: int) -> List[Conversacion]:
        return self.conversacion_repository.listar_por_usuario(usuario_id)


class EliminarConversacion:
    def __init__(self, conversacion_repository: ConversacionRepository):
        self.conversacion_repository = conversacion_repository

    def execute(self, conversacion_id: int) -> None:
        self.conversacion_repository.eliminar(conversacion_id)
