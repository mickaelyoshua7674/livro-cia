from pydantic import BaseModel
from livro import Livro
from datetime import datetime

class Venda(BaseModel):
    livro: Livro
    valor_unitario: float
    quantidade: int
    data: datetime