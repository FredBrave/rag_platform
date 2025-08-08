from dataclasses import dataclass
from typing import Optional

@dataclass
class APIKey:
    id: Optional[int]
    usuario_id: int
    proveedor: str
    clave: str
    activa: bool