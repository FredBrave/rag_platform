# repositories/django_rag_permiso_repository.py
from typing import List
from ..models import RAGPermiso
from core.repositories.rag_respository import RAGPermisoRepository

class DjangoRAGPermisoRepository(RAGPermisoRepository):
    
    def get_permisos_por_rag(self, rag_id: int) -> List[RAGPermiso]:
        return list(RAGPermiso.objects.filter(rag_id=rag_id))
    
    def puede_usuario_editar(self, rag_id: int, usuario_id: int) -> bool:
        return RAGPermiso.objects.filter(
            rag_id=rag_id,
            usuario_id=usuario_id,
            puede_editar=True
        ).exists()
    
    def crear_permiso(self, permiso: RAGPermiso) -> RAGPermiso:
        permiso.save()
        return permiso
    
    def eliminar_permiso(self, permiso_id: int) -> None:
        RAGPermiso.objects.filter(id=permiso_id).delete()
