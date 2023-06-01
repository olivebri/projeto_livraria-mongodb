from model.categoria import Categoria
from model.editora import Editora
from model.autor import Autor
from bson import ObjectId
import random
import string

class Livro:

    def __init__(self, titulo: str, resumo: str, ano: int, paginas: int, isbn: str, categoria: Categoria, editora: Editora, autor: Autor):
        self.__id: ObjectId = None
        self.__titulo: str = titulo
        self.__resumo: str = resumo
        self.__ano: int = ano
        self.__paginas: int = paginas
        self.__isbn: str = isbn
        self.__codigo: str = self.__gerar_codigo(categoria)
        self.__categoria: Categoria = categoria
        self.__editora: Editora = editora
        self.__autor: Autor = autor

    @property
    def id(self) -> ObjectId:
        return self.__id
    
    @id.setter
    def id(self, id: ObjectId):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        self.__categoria = categoria

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor

    def __gerar_codigo(self, categoria: Categoria) -> str:
        rand = random.choices(string.ascii_uppercase + string.digits, k=7)
        return categoria.nome[0:3].upper() + ''.join(rand)