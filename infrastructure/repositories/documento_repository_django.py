# infraestructura/repositorios/documento_repository_impl.py
from core.repositories.documento_repository import DocumentoRepository
from core.models_domain.documentos import Documento
from models.documentos import DocumentoModel

class DocumentoRepositoryDjango(DocumentoRepository):

    def guardar(self, documento: Documento) -> None:
        DocumentoModel.objects.create(
            id=documento.id,
            nombre=documento.nombre,
            contenido=documento.contenido
        )

    def obtener_por_id(self, documento_id: str) -> Documento:
        doc = DocumentoModel.objects.get(id=documento_id)
        return Documento(id=doc.id, nombre=doc.nombre, contenido=doc.contenido)

    def listar(self):
        docs = DocumentoModel.objects.only("id", "nombre")
        return [Documento(id=doc.id, nombre=doc.nombre, contenido=None) for doc in docs]
    
    def eliminar(self, documento_id: str) -> None:
        DocumentoModel.objects.filter(id=documento_id).delete()
