from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    id: Optional[int]
    username: str
    email: str
    foto_perfil_url: Optional[str]
    plan: str
    password: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            email=data.get("email"),
            foto_perfil_url=data.get("foto_perfil_url"),
            plan=data.get("plan"),
            password=data.get("password")
        )