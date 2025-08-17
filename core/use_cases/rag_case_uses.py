from typing import List, Optional
from core.models_domain.rag import RAG
from core.repositories.rag_respository import RAGRepository
from datetime import datetime

class CrearRAG:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, nombre: str, descripcion: str, privacidad: bool, creador_id: int, modelo_llm: str, embedding_model: str) -> RAG:
        ahora = datetime.now()
        nuevo_rag = RAG(
            id=None,
            nombre=nombre,
            descripcion=descripcion,
            privacidad=privacidad,
            creador_id=creador_id,
            modelo_llm=modelo_llm,
            embedding_model=embedding_model,
            fecha_creacion=ahora,
            fecha_actualizacion=ahora,
        )
        return self.rag_repository.guardar(nuevo_rag)


class ObtenerRagPorId:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, rag_id):
        rag = self.repository.obtener_por_id(rag_id)
        if not rag:
            raise ValueError(f"RAG con id {rag_id} no encontrado")
        return rag

class ListarRAGsPorUsuario:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, creador_id: int) -> List[RAG]:
        return self.rag_repository.listar_por_usuario(creador_id)

class ListarRAGsPorPrivacidad:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, privacidad: bool) -> List[RAG]:
        return self.rag_repository.listar_por_privacidad(privacidad)

class EliminarRAG:
    def __init__(self, rag_repository: RAGRepository):
        self.rag_repository = rag_repository

    def execute(self, rag_id: int) -> None:
        self.rag_repository.eliminar(rag_id)