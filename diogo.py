from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List

Base = declarative_base()

class Endereco(Base):
    __tablename__ = "endereco"
    id = Column(Integer, primary_key=True, index=True)
    rua = Column(String(255), index=True)
    
    id_pessoa = Column(Integer(), ForeignKey('pessoa.id'), nullable=False)


class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), index=True)
    
    enderecos = relationship("Endereco", backref="pessoa")



class EnderecoSchema(BaseModel):
    id: int = 1
    rua: str = "Teste"

    class Config:
        orm_mode = True


class PessoaSchema(BaseModel):
    id: int
    name: str = ""

    enderecos: List[EnderecoSchema] = None

    class Config:
        orm_mode = True
    
temp = PessoaSchema(id=1, name="teste", enderecos=[EnderecoSchema()])
pessoa = Pessoa()
for k, v in temp.dict().items():
    print(k,v)
    setattr(pessoa, k, v)

Pessoa(**temp.__dict__)
