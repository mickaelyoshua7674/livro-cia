from pydantic import BaseModel

class Livro(BaseModel):
    nome: str
    valor_compra: float
    valor_venda: float