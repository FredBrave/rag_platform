from typing import List, Optional
from core.models_domain.embedding import Embedding
from core.repositories.embedding_repository import EmbeddingRepository
from openai import OpenAI


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

class GenerarEmbeddingsRAG:
    def __init__(self, documento_repository, embedding_repository):
        self.documento_repository = documento_repository
        self.embedding_repository = embedding_repository
        self.client = OpenAI()

    def dividir_texto(self, texto, chunk_size=500, overlap=50):
        """Divide el texto en chunks con solapamiento"""
        palabras = texto.split()
        chunks = []
        i = 0
        while i < len(palabras):
            chunk = palabras[i:i+chunk_size]
            chunks.append(" ".join(chunk))
            i += chunk_size - overlap
        return chunks

    def procesar_documento(self, documento):
        texto = self.documento_repository.extraer_texto(documento)
        chunks = self.dividir_texto(texto)

        for i, chunk in enumerate(chunks):
            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            )
            vector = response.data[0].embedding

            embedding = Embedding(
                documento_id=documento.id,
                texto_fragmento=chunk,
                vector=vector,
                indice=i
            )
            self.embedding_repository.guardar(embedding)

    def execute(self, rag_id: int):
        documentos = self.documento_repository.listar_por_rag(rag_id)
        for doc in documentos:
            self.procesar_documento(doc)


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
