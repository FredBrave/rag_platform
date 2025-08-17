from typing import List, Optional
from core.models_domain.rag import RAG
from core.repositories.rag_respository import RAGRepository
from infrastructure.models.rag import RAG as RAGORM 

class RagRepositoryDjango(RAGRepository):
    def guardar(self, rag: RAG) -> RAG:
        """Guarda o actualiza un RAG desde el modelo de dominio."""
        if rag.id:
            rag_obj = RAGORM.objects.get(pk=rag.id)
            rag_obj.nombre = rag.nombre
            rag_obj.descripcion = rag.descripcion
            rag_obj.creador_id = rag.creador_id
            rag_obj.privacidad = rag.privacidad
            rag_obj.modelo_llm = rag.modelo_llm
            rag_obj.embedding_model = rag.embedding_model
            rag_obj.save()
        else:
            rag_obj = RAGORM.objects.create(
                nombre=rag.nombre,
                descripcion=rag.descripcion,
                creador_id=rag.creador_id,
                privacidad=rag.privacidad,
                modelo_llm=rag.modelo_llm,
                embedding_model=rag.embedding_model,
                fecha_creacion=rag.fecha_creacion,
            )
        return RAG(
            id=rag_obj.id,
            nombre=rag_obj.nombre,
            descripcion=rag_obj.descripcion,
            creador_id=rag_obj.creador_id,
            privacidad=rag_obj.privacidad,
            modelo_llm=rag_obj.modelo_llm,
            embedding_model=rag_obj.embedding_model,
            fecha_creacion=rag_obj.fecha_creacion,
            fecha_actualizacion=rag_obj.fecha_actualizacion
        )

    def obtener_por_id(self, rag_id: int) -> Optional[RAG]:
        try:
            rag_obj = RAGORM.objects.get(pk=rag_id)
            return RAG(
                id=rag_obj.id,
                nombre=rag_obj.nombre,
                descripcion=rag_obj.descripcion,
                creador_id=rag_obj.creador_id,
                privacidad=rag_obj.privacidad,
                modelo_llm=rag_obj.modelo_llm,
                embedding_model=rag_obj.embedding_model,
                fecha_creacion=rag_obj.fecha_creacion,
                fecha_actualizacion=rag_obj.fecha_actualizacion
            )
        except RAGORM.DoesNotExist:
            return None
    def listar_por_usuario(self, creador_id: int) -> List[RAG]:
        """Devuelve una lista de RAGs para un usuario específico."""
        rag_objs = RAGORM.objects.filter(creador_id=creador_id)
        return [
            RAG(
                id=obj.id,
                nombre=obj.nombre,
                descripcion=obj.descripcion,
                creador_id=obj.creador_id,
                privacidad=obj.privacidad,
                modelo_llm=obj.modelo_llm,
                embedding_model=obj.embedding_model,
                fecha_creacion=obj.fecha_creacion,
                fecha_actualizacion=obj.fecha_actualizacion
            )
            for obj in rag_objs
        ]
    
    def listar_por_privacidad(self, privacidad: str):
        queryset = RAGORM.objects.filter(privacidad=privacidad)
        rags = [
            RAG(
                id=r.id,
                nombre=r.nombre,
                descripcion=r.descripcion,
                creador_id=r.creador.id,
                privacidad=r.privacidad,
                modelo_llm=r.modelo_llm,
                embedding_model=r.embedding_model,
                fecha_creacion=r.fecha_creacion,
                fecha_actualizacion=r.fecha_actualizacion,
            )
            for r in queryset
        ]
        return rags

    def eliminar(self, rag_id: int) -> bool:
        """Elimina un RAG por ID. Devuelve True si se eliminó, False si no existía."""
        try:
            rag_obj = RAGORM.objects.get(pk=rag_id)
            rag_obj.delete()
            return True
        except RAGORM.DoesNotExist:
            return False