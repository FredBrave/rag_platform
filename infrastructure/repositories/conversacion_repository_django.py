from typing import List, Optional
from core.models_domain.conversaciones import Conversacion
from core.repositories.conversacion_repository import ConversacionRepository
from models.conversaciones import Conversacion as ConversacionORM

class ConversacionRepositoryDjango(ConversacionRepository):

    def guardar(self, conversacion: Conversacion) -> Conversacion:
        if conversacion.id:
            obj = ConversacionORM.objects.get(id=conversacion.id)
            obj.rag_id = conversacion.rag_id
            obj.usuario_id = conversacion.usuario_id
            obj.titulo = conversacion.titulo
            obj.fecha_creacion = conversacion.fecha_creacion
            obj.save()
        else:
            obj = ConversacionORM.objects.create(
                rag_id=conversacion.rag_id,
                usuario_id=conversacion.usuario_id,
                titulo=conversacion.titulo,
                fecha_creacion=conversacion.fecha_creacion
            )
            conversacion.id = obj.id
        return conversacion

    def obtener_por_id(self, conversacion_id: int) -> Optional[Conversacion]:
        try:
            obj = ConversacionORM.objects.get(id=conversacion_id)
            return Conversacion(
                id=obj.id,
                rag_id=obj.rag_id,
                usuario_id=obj.usuario_id,
                titulo=obj.titulo,
                fecha_creacion=obj.fecha_creacion
            )
        except ConversacionORM.DoesNotExist:
            return None

    def listar_por_usuario(self, usuario_id: int) -> List[Conversacion]:
        objs = ConversacionORM.objects.filter(usuario_id=usuario_id)
        return [
            Conversacion(
                id=obj.id,
                rag_id=obj.rag_id,
                usuario_id=obj.usuario_id,
                titulo=obj.titulo,
                fecha_creacion=obj.fecha_creacion
            ) for obj in objs
        ]

    def eliminar(self, conversacion_id: int) -> None:
        ConversacionORM.objects.filter(id=conversacion_id).delete()