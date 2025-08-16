from typing import List, Optional
from core.models_domain.embedding import Embedding
from core.repositories.embedding_repository import EmbeddingRepository
from infrastructure.models.embedding import Embedding as EmbeddingORM

class EmbeddingRepositoryDjango(EmbeddingRepository):

    def guardar(self, embedding: Embedding) -> Embedding:
        if embedding.id is not None:
            obj = EmbeddingORM.objects.get(id=embedding.id)
            obj.documento_id = embedding.documento_id
            obj.texto_fragmento = embedding.texto_fragmento
            obj.vector = embedding.vector
            obj.indice = embedding.indice
            obj.save()
        else:
            obj = EmbeddingORM.objects.create(
                documento_id=embedding.documento_id,
                texto_fragmento=embedding.texto_fragmento,
                vector=embedding.vector,
                indice=embedding.indice
            )
            embedding.id = obj.id
        return embedding

    def listar_por_documento(self, documento_id: int) -> List[Embedding]:
        objs = EmbeddingORM.objects.filter(documento_id=documento_id)
        return [
            Embedding(
                id=obj.id,
                documento_id=obj.documento_id,
                texto_fragmento=obj.texto_fragmento,
                vector=obj.vector,
                indice=obj.indice
            ) for obj in objs
        ]

    def obtener_por_id(self, embedding_id: int) -> Optional[Embedding]:
        try:
            obj = EmbeddingORM.objects.get(id=embedding_id)
            return Embedding(
                id=obj.id,
                documento_id=obj.documento_id,
                texto_fragmento=obj.texto_fragmento,
                vector=obj.vector,
                indice=obj.indice
            )
        except EmbeddingORM.DoesNotExist:
            return None

    def eliminar_por_documento(self, documento_id: int) -> None:
        EmbeddingORM.objects.filter(documento_id=documento_id).delete()