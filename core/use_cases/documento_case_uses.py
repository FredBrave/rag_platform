from core.models_domain.documentos import Documento
from core.repositories.documento_repository import DocumentoRepository

class CrearDocumento:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def ejecutar(self, id: str, nombre: str, contenido: str):
        documento = Documento(id=id, nombre=nombre, contenido=contenido)
        self.repository.guardar(documento)
        return documento


class ObtenerDocumento:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def ejecutar(self, documento_id: str) -> Documento:
        return self.repository.obtener_por_id(documento_id)


class ListarDocumentos:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def ejecutar(self):
        return self.repository.listar()


class EliminarDocumento:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def ejecutar(self, documento_id: str):
        self.repository.eliminar(documento_id)
