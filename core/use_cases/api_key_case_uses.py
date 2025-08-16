from typing import List, Optional
from datetime import datetime
from core.models_domain.api_keys import APIKey
from core.repositories.api_key_repository import APIKeyRepository


class CrearAPIKey:
    def __init__(self, api_key_repository: APIKeyRepository):
        self.api_key_repository = api_key_repository

    def execute(self, usuario_id: int, proveedor: str, clave: str) -> APIKey:
        nueva_key = APIKey(
            id=None,
            usuario_id=usuario_id,
            proveedor=proveedor,
            clave=clave,
            activa=True,
            eliminado=False,
            fecha_creacion=datetime.now(),
            fecha_actualizacion=datetime.now(),
        )
        return self.api_key_repository.guardar(nueva_key)


class ObtenerAPIKeyPorId:
    def __init__(self, api_key_repository: APIKeyRepository):
        self.api_key_repository = api_key_repository

    def execute(self, api_key_id: int) -> Optional[APIKey]:
        return self.api_key_repository.obtener_por_id(api_key_id)


class ListarAPIKeysPorUsuario:
    def __init__(self, api_key_repository: APIKeyRepository):
        self.api_key_repository = api_key_repository

    def execute(self, usuario_id: int) -> List[APIKey]:
        return self.api_key_repository.listar_por_usuario(usuario_id)


class DesactivarAPIKey:
    def __init__(self, api_key_repository: APIKeyRepository):
        self.api_key_repository = api_key_repository

    def execute(self, api_key_id: int) -> Optional[APIKey]:
        api_key = self.api_key_repository.obtener_por_id(api_key_id)
        if api_key:
            api_key.activa = False
            api_key.fecha_actualizacion = datetime.now()
            return self.api_key_repository.guardar(api_key)
        return None


class EliminarAPIKey:
    def __init__(self, api_key_repository: APIKeyRepository):
        self.api_key_repository = api_key_repository

    def execute(self, api_key_id: int) -> Optional[APIKey]:
        api_key = self.api_key_repository.obtener_por_id(api_key_id)
        if api_key:
            api_key.eliminado = True
            api_key.fecha_actualizacion = datetime.now()
            return self.api_key_repository.guardar(api_key)
        return None
