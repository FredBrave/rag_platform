from dataclasses import dataclass
from typing import Optional
from typing import List

@dataclass
class Embedding:
    id: Optional[int]
    documento_id: int
    texto_fragmento: str
    vector: List[float]
    indice: int

    def similitud_coseno(self, otro_vector: List[float]) -> float:
        """Calcula la similitud del vector con otro vector."""
        import numpy as np
        v1 = np.array(self.vector)
        v2 = np.array(otro_vector)
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))