from typing import List
from core.models_domain.conversaciones import Mensaje
from core.repositories.conversacion_repository import MensajeRepository
from models.conversaciones import Mensaje as MensajeORM

class MensajeRepositoryDjango(MensajeRepository):

    def guardar(self, mensaje: Mensaje) -> Mensaje:
        if mensaje.id:
            obj = MensajeORM.objects.get(id=mensaje.id)
            obj.conversacion_id = mensaje.conversacion_id
            obj.rol = mensaje.rol
            obj.contenido = mensaje.contenido
            obj.fecha = mensaje.fecha
            obj.save()
        else:
            obj = MensajeORM.objects.create(
                conversacion_id=mensaje.conversacion_id,
                rol=mensaje.rol,
                contenido=mensaje.contenido,
                fecha=mensaje.fecha
            )
            mensaje.id = obj.id
        return mensaje

    def listar_por_conversacion(self, conversacion_id: int) -> List[Mensaje]:
        objs = MensajeORM.objects.filter(conversacion_id=conversacion_id).order_by('fecha')
        return [
            Mensaje(
                id=obj.id,
                conversacion_id=obj.conversacion_id,
                rol=obj.rol,
                contenido=obj.contenido,
                fecha=obj.fecha
            ) for obj in objs
        ]

    def eliminar_por_conversacion(self, conversacion_id: int) -> None:
        MensajeORM.objects.filter(conversacion_id=conversacion_id).delete()