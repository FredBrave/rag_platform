from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Conversacion:
    id: Optional[int]
    rag_id: int
    usuario_id: int
    titulo: str
    fecha_creacion: Optional[datetime] = None

@dataclass
class Mensaje:
    id: Optional[int]
    conversacion_id: int
    rol: str
    contenido: str
    fecha: datetime