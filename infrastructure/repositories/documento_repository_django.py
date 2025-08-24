# infraestructura/repositorios/documento_repository_impl.py
from core.repositories.documento_repository import DocumentoRepository
from core.models_domain.documentos import Documento
from infrastructure.models.documentos import Documento as DocumentoORM
from infrastructure.models.rag import RAG
import PyPDF2, docx

class DocumentoRepositoryDjango(DocumentoRepository):

    def guardar(self, documento: Documento) -> None:
        rag_instance = RAG.objects.get(id=documento.rag_id)
        DocumentoORM.objects.create(
            id=documento.id,
            rag = rag_instance,
            nombre=documento.nombre,
            archivo=documento.archivo,
            texto_extraido=documento.texto_extraido,
            fecha_subida=documento.fecha_subida
        )

    def obtener_por_id(self, documento_id: str) -> Documento:
        doc = DocumentoORM.objects.get(id=documento_id)
        return Documento(id=doc.id, nombre=doc.nombre, texto_extraido=None, rag_id=doc.rag_id, archivo=doc.archivo)

    def listar(self):
        docs = DocumentoORM.objects.only("id", "nombre")
        return [Documento(id=doc.id, nombre=doc.nombre, texto_extraido=None, rag_id=doc.rag_id, archivo=doc.archivo) for doc in docs]
    

    def listar_por_rag(self, rag_id: int):
        return Documento.objects.filter(rag_id=rag_id)

    def extraer_texto(self, documento: Documento) -> str:
        if documento.tipo == "pdf":
            texto = ""
            with open(documento.archivo.path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    texto += page.extract_text() + "\n"
            return texto

        elif documento.tipo == "txt":
            with open(documento.archivo.path, "r", encoding="utf-8") as f:
                return f.read()

        elif documento.tipo == "docx":
            doc = docx.Document(documento.archivo.path)
            return "\n".join([p.text for p in doc.paragraphs])

        return ""
    
    def eliminar(self, documento_id: str) -> None:
        DocumentoORM.objects.filter(id=documento_id).delete()
