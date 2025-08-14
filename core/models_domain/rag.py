from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class RAG:
    id: Optional[int]
    nombre: str
    descripcion: str
    creador_id: int
    privacidad: bool
    modelo_llm: str
    embedding_model: str
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

@dataclass
class RAGPermiso:
    id: int | None
    rag_id: int
    creador_id: int
    puede_editar: bool