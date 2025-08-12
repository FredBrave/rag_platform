# usecases/rag_permiso_usecases.py
from typing import List
from core.models_domain.rag import RAGPermiso
from core.repositories.rag_respository import RAGPermisoRepository

class ObtenerPermisosPorRAG:
    def __init__(self, repo: RAGPermisoRepository):
        self.repo = repo

    def ejecutar(self, rag_id: int) -> List[RAGPermiso]:
        return self.repo.get_permisos_por_rag(rag_id)


class PuedeUsuarioEditarRAG:
    def __init__(self, repo: RAGPermisoRepository):
        self.repo = repo

    def ejecutar(self, rag_id: int, usuario_id: int) -> bool:
        return self.repo.puede_usuario_editar(rag_id, usuario_id)


class CrearPermisoRAG:
    def __init__(self, repo: RAGPermisoRepository):
        self.repo = repo

    def ejecutar(self, rag_id: int, usuario_id: int, puede_editar: bool) -> RAGPermiso:
        permiso = RAGPermiso(
            rag_id=rag_id,
            usuario_id=usuario_id,
            puede_editar=puede_editar
        )
        return self.repo.crear_permiso(permiso)


class EliminarPermisoRAG:
    def __init__(self, repo: RAGPermisoRepository):
        self.repo = repo

    def ejecutar(self, permiso_id: int) -> None:
        self.repo.eliminar_permiso(permiso_id)
