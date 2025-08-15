from core.models_domain.rag import RAG, RAGPermiso
from abc import ABC, abstractmethod
from typing import List, Optional


class RAGPermisoRepository(ABC):

    @abstractmethod
    def get_permisos_por_rag(self, rag_id: int) -> List[RAGPermiso]:
        pass

    @abstractmethod
    def puede_usuario_editar(self, rag_id: int, usuario_id: int) -> bool:
        pass

    @abstractmethod
    def crear_permiso(self, permiso: RAGPermiso) -> RAGPermiso:
        pass

    @abstractmethod
    def eliminar_permiso(self, permiso_id: int) -> None:
        pass


class RAGRepository(ABC):

    @abstractmethod
    def guardar(self, rag: RAG) -> RAG:
        """Guarda o actualiza un RAG y devuelve la entidad guardada."""
        pass

    @abstractmethod
    def obtener_por_id(self, rag_id: int) -> Optional[RAG]:
        """Obtiene un RAG por su ID, o None si no existe."""
        pass

    @abstractmethod
    def listar_por_usuario(self, creador_id: int) -> List[RAG]:
        """Lista todos los RAGs que pertenecen a un usuario."""
        pass

    @abstractmethod
    def eliminar(self, rag_id: int) -> None:
        """Elimina un RAG dado su ID."""
        pass