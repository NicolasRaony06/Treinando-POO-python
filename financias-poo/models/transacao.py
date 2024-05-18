from dataclasses import dataclass
from models.categoria import Categoria

@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria