from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class APIKey:
    id: Optional[int]
    usuario_id: int
    proveedor: str
    clave: str
    activa: bool
    eliminado: bool
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None