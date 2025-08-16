# infraestructura/repositorios/documento_repository_impl.py
from core.repositories.documento_repository import DocumentoRepository
from core.models_domain.documentos import Documento
from infrastructure.models.documentos import Documento as DocumentoORM
from infrastructure.models.rag import RAG

class DocumentoRepositoryDjango(DocumentoRepository):

    def guardar(self, documento: Documento) -> None:
        rag_instance = RAG.objects.get(id=documento.rag_id)
        DocumentoORM.objects.create(
            id=documento.id,
            rag = rag_instance,
            nombre=documento.nombre,
            texto_extraido=documento.texto_extraido,
            fecha_subida=documento.fecha_subida
        )

    def obtener_por_id(self, documento_id: str) -> Documento:
        doc = DocumentoORM.objects.get(id=documento_id)
        return Documento(id=doc.id, nombre=doc.nombre, texto_extraido=doc.texto_extraido)

    def listar(self):
        docs = DocumentoORM.objects.only("id", "nombre")
        return [Documento(id=doc.id, nombre=doc.nombre, texto_extraido=None) for doc in docs]
    
    def eliminar(self, documento_id: str) -> None:
        DocumentoORM.objects.filter(id=documento_id).delete()
