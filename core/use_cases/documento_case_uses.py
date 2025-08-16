from core.models_domain.documentos import Documento
from core.repositories.documento_repository import DocumentoRepository
from datetime import datetime
class CrearDocumento:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def execute(self, rag_id: int, nombre: str, archivo: str):
        now = datetime.now()
        documento = Documento(id=None, rag_id=rag_id, nombre=nombre, archivo=archivo, texto_extraido=None, fecha_subida=now)
        self.repository.guardar(documento)
        return documento


class ObtenerDocumento:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def execute(self, documento_id: str) -> Documento:
        return self.repository.obtener_por_id(documento_id)


class ListarDocumentos:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def execute(self):
        return self.repository.listar()


class EliminarDocumento:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def execute(self, documento_id: str):
        self.repository.eliminar(documento_id)
