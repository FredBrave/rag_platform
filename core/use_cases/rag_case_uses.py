# application/services/rag_service.py
from typing import List, Optional
from core.models_domain.rag import RAG
from core.repositories.rag_respository import RAGRepository

class CrearRAG:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, nombre: str, descripcion: str, privado: bool, usuario_id: int) -> RAG:
        nuevo_rag = RAG(
            id=None,
            nombre=nombre,
            descripcion=descripcion,
            privado=privado,
            usuario_id=usuario_id
        )
        return self.rag_repository.guardar(nuevo_rag)


class ObtenerRAGPorId:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, rag_id: int) -> Optional[RAG]:
        return self.rag_repository.obtener_por_id(rag_id)


class ListarRAGsPorUsuario:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, usuario_id: int) -> List[RAG]:
        return self.rag_repository.listar_por_usuario(usuario_id)


class EliminarRAG:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, rag_id: int) -> None:
        self.rag_repository.eliminar(rag_id)