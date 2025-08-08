from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    id: Optional[int]
    username: str
    email: str
    foto_perfil_url: Optional[str]
    plan: str