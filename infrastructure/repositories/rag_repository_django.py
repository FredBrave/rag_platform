from typing import List, Optional
from core.models_domain.rag import RAG
from core.repositories.rag_respository import RAGRepository
from infrastructure.models.rag import RAG as RAGORM 

class RAGRepositoryDjango(RAGRepository):

    def guardar(self, rag: RAG) -> RAG:
        if rag.id is not None:
            obj = RAGORM.objects.get(id=rag.id)
            obj.nombre = rag.nombre
            obj.descripcion = rag.descripcion
            obj.privacidad = rag.privacidad
            obj.creador_id = rag.creador_id
            obj.save()
        else:
            obj = RAGORM.objects.create(
                nombre=rag.nombre,
                descripcion=rag.descripcion,
                privacidad=rag.privacidad,
                creador_id=rag.creador_id
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
                privacidad=obj.privacidad,
                creador_id=obj.creador_id
            )
        except RAGORM.DoesNotExist:
            return None

    def listar_por_usuario(self, usuario_id: int) -> List[RAG]:
        objs = RAGORM.objects.filter(creador_id=usuario_id)
        return [
            RAG(
                id=obj.id,
                nombre=obj.nombre,
                descripcion=obj.descripcion,
                privacidad=obj.privacidad,
                creador_id=obj.creador_id,
                modelo_llm=obj.modelo_llm,
                embedding_model=obj.embedding_model
            ) for obj in objs
        ]

    def eliminar(self, rag_id: int) -> None:
        RAGORM.objects.filter(id=rag_id).delete()