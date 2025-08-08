# dominio/repositorios/documento_repository.py
from abc import ABC, abstractmethod
from typing import List
from core.models_domain.documentos import Documento

class DocumentoRepository(ABC):

    @abstractmethod
    def guardar(self, documento: Documento) -> None:
        """Guarda un documento."""
        pass

    @abstractmethod
    def obtener_por_id(self, documento_id: str) -> Documento:
        """Obtiene un documento por su ID."""
        pass

    @abstractmethod
    def listar(self) -> List[Documento]:
        """Lista todos los documentos."""
        pass