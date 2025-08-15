from typing import List
from core.models_domain.rag import RAGPermiso as RAGPermisoDomain
from core.repositories.rag_respository import RAGPermisoRepository
from infrastructure.models.rag import RAGPermiso as RAGPermisoORM

class RAGPermisoRepositoryDjango(RAGPermisoRepository):
    
    def get_permisos_por_rag(self, rag_id: int) -> List[RAGPermisoDomain]:
        permisos_orm = RAGPermisoORM.objects.filter(rag_id=rag_id)
        return [
            RAGPermisoDomain(
                id=p.id,
                rag_id=p.rag_id,
                usuario_id=p.usuario_id,
                puede_editar=p.puede_editar
            )
            for p in permisos_orm
        ]
    
    def puede_usuario_editar(self, rag_id: int, usuario_id: int) -> bool:
        return RAGPermisoORM.objects.filter(
            rag_id=rag_id,
            usuario_id=usuario_id,
            puede_editar=True
        ).exists()
    
    def crear_permiso(self, permiso: RAGPermisoDomain) -> RAGPermisoDomain:
        obj = RAGPermisoORM.objects.create(
            rag_id=permiso.rag_id,
            usuario_id=permiso.usuario_id,
            puede_editar=permiso.puede_editar
        )
        permiso.id = obj.id
        return permiso
    
    def eliminar_permiso(self, permiso_id: int) -> None:
        RAGPermisoORM.objects.filter(id=permiso_id).delete()