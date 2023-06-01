from model.autor import Autor
from database.client_factory import ClientFactory
from bson import ObjectId

class AutorDAO:

    def __init__(self):
        self.__client_factory: ClientFactory = ClientFactory()

    def listar(self) -> list[Autor]:
        autores = list()

        client = self.__client_factory.get_client()
        db = client.livraria
        for documento in db.autores.find():
            aut = Autor(documento['nome'], documento['email'], 
                          documento['telefone'], documento['bio'])
            aut.id = documento['_id']
            autores.append(aut)
        client.close()

        return autores

    def adicionar(self, autor: Autor) -> None:
        client = self.__client_factory.get_client()
        db = client.livraria
        db.autores.insert_one({
            'nome': autor.nome, 
            'email': autor.email, 
            'telefone': autor.telefone,
            'bio': autor.bio})
        client.close()

    def remover(self, autor_id: str) -> bool:
        client = self.__client_factory.get_client()
        db = client.livraria
        resultado = db.autores.delete_one({'_id': ObjectId(autor_id)})
        if (resultado.deleted_count == 1):
            return True
        return False

    def buscar_por_id(self, autor_id: str) -> Autor:
        aut = None
        client = self.__client_factory.get_client()
        db = client.livraria
        resultado = db.autores.find_one({'_id': ObjectId(autor_id)})
        if (resultado):
            aut = Autor(resultado['nome'], resultado['email'], 
                          resultado['telefone'], resultado['bio'])
            aut.id = resultado['_id']
        client.close()
        return aut
    