from typing import List, Optional
from core.models_domain.rag import RAG
from core.repositories.rag_respository import RAGRepository
from models.rag import RAG as RAGORM 

class RAGRepositoryDjango(RAGRepository):

    def guardar(self, rag: RAG) -> RAG:
        if rag.id is not None:
            obj = RAGORM.objects.get(id=rag.id)
            obj.nombre = rag.nombre
            obj.descripcion = rag.descripcion
            obj.privado = rag.privado
            obj.usuario_id = rag.usuario_id
            obj.save()
        else:
            obj = RAGORM.objects.create(
                nombre=rag.nombre,
                descripcion=rag.descripcion,
                privado=rag.privado,
                usuario_id=rag.usuario_id
            )
            rag.id = obj.id
        return rag

    def obtener_por_id(self, rag_id: int) -> Optional[RAG]:
        try:
            obj = RAGORM.objects.get(id=rag_id)
            return RAG(
                id=obj.id,
                nombre=obj.nombre,
                descripcion=obj.descripcion,
                privado=obj.privado,
                usuario_id=obj.usuario_id
            )
        except RAGORM.DoesNotExist:
            return None

    def listar_por_usuario(self, usuario_id: int) -> List[RAG]:
        objs = RAGORM.objects.filter(usuario_id=usuario_id)
        return [
            RAG(
                id=obj.id,
                nombre=obj.nombre,
                descripcion=obj.descripcion,
                privado=obj.privado,
                usuario_id=obj.usuario_id
            ) for obj in objs
        ]

    def eliminar(self, rag_id: int) -> None:
        RAGORM.objects.filter(id=rag_id).delete()