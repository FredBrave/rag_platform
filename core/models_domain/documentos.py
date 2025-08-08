from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Documento:
    id: Optional[id]
    rag_id: int
    nombre: str
    archivo: str
    texto_extraido: str
    fecha_subida: Optional[datetime] = None