from typing import List, Optional
from core.models_domain.api_keys import APIKey
from core.repositories.api_key_repository import APIKeyRepository
from core.models.api_keys import APIKey as APIKeyORM

class APIKeyRepositoryDjango(APIKeyRepository):

    def guardar(self, api_key: APIKey) -> APIKey:
        if api_key.id is not None:
            obj = APIKeyORM.objects.get(id=api_key.id)
            obj.usuario_id = api_key.usuario_id
            obj.proveedor = api_key.proveedor
            obj.clave = api_key.clave
            obj.activa = api_key.activa
            obj.save()
        else:
            obj = APIKeyORM.objects.create(
                usuario_id=api_key.usuario_id,
                proveedor=api_key.proveedor,
                clave=api_key.clave,
                activa=api_key.activa
            )
            api_key.id = obj.id
        return api_key

    def obtener_por_id(self, api_key_id: int) -> Optional[APIKey]:
        try:
            obj = APIKeyORM.objects.get(id=api_key_id)
            return APIKey(
                id=obj.id,
                usuario_id=obj.usuario_id,
                proveedor=obj.proveedor,
                clave=obj.clave,
                activa=obj.activa
            )
        except APIKeyORM.DoesNotExist:
            return None

    def listar_por_usuario(self, usuario_id: int) -> List[APIKey]:
        objs = APIKeyORM.objects.filter(usuario_id=usuario_id, activa=True)
        return [
            APIKey(
                id=obj.id,
                usuario_id=obj.usuario_id,
                proveedor=obj.proveedor,
                clave=obj.clave,
                activa=obj.activa
            ) for obj in objs
        ]

    def desactivar(self, api_key_id: int) -> None:
        obj = APIKeyORM.objects.get(id=api_key_id)
        obj.activa = False
        obj.save()

    def eliminar(self, api_key_id: int) -> None:
        APIKeyORM.objects.filter(id=api_key_id).delete()