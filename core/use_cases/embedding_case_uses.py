from typing import List, Optional
from core.models_domain.embedding import Embedding
from core.repositories.embedding_repository import EmbeddingRepository


class CrearEmbedding:
    def __init__(self, repository: EmbeddingRepository):
        self.repository = repository

    def execute(self, documento_id: int, texto_fragmento: str, vector: list, indice: int) -> Embedding:
        embedding = Embedding(
            documento_id=documento_id,
            texto_fragmento=texto_fragmento,
            vector=vector,
            indice=indice
        )
        return self.repository.guardar(embedding)


class ListarEmbeddingsPorDocumento:
    def __init__(self, repository: EmbeddingRepository):
        self.repository = repository

    def execute(self, documento_id: int) -> List[Embedding]:
        return self.repository.listar_por_documento(documento_id)


class ObtenerEmbeddingPorId:
    def __init__(self, repository: EmbeddingRepository):
        self.repository = repository

    def execute(self, embedding_id: int) -> Optional[Embedding]:
        return self.repository.obtener_por_id(embedding_id)


class EliminarEmbeddingsPorDocumento:
    def __init__(self, repository: EmbeddingRepository):
        self.repository = repository

    def execute(self, documento_id: int) -> None:
        self.repository.eliminar_por_documento(documento_id)
