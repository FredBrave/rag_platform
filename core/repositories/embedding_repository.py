from abc import ABC, abstractmethod
from typing import List, Optional
from core.models_domain.embedding import Embedding

class EmbeddingRepository(ABC):

    @abstractmethod
    def guardar(self, embedding: Embedding) -> Embedding:
        """Guarda o actualiza un embedding y devuelve la entidad guardada."""
        pass

    @abstractmethod
    def listar_por_documento(self, documento_id: int) -> List[Embedding]:
        """Devuelve todos los embeddings asociados a un documento."""
        pass

    @abstractmethod
    def obtener_por_id(self, embedding_id: int) -> Optional[Embedding]:
        """Obtiene un embedding por su ID."""
        pass

    @abstractmethod
    def eliminar_por_documento(self, documento_id: int) -> None:
        """Elimina todos los embeddings asociados a un documento."""
        pass