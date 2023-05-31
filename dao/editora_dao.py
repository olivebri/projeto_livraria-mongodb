from model.editora import Editora
from database.client_factory import ClientFactory
from bson import ObjectId


class EditoraDAO:

    def __init__(self):
        self.__client_factory: ClientFactory = ClientFactory()
        self.__editoras: list[Editora] = list()

    def listar(self) -> list[Editora]:
        editoras = list()
        client = self.__client_factory.get_client()
        db = client.livraria

        for documento in db.editoras.find():
            edt = Editora(documento['nome'],documento['endereco'], documento['telefone'])
            edt.id = documento['_id']
            editoras.append(edt)
        
        client.close
        return editoras

    def adicionar(self, editora: Editora) -> None:
        client = self.__client_factory.get_client()
        db = client.livraria
        db.editoras.insert_one({
            'nome': editora.nome,
            'telefone': editora.telefone,
            'endereco': editora.endereco
        })

        client.close()


    def remover(self, editora_id: str) -> bool:
        client = self.__client_factory.get_client()
        db = client.livraria

        resultado = db.editoras.delete_one(
            {'_id': ObjectId(editora_id)}
        )

        if (resultado.deleted_count == 1):
            return True
        return False


    def buscar_por_id(self, editora_id) -> Editora:
        edt = None
        client = self.__client_factory.get_client()
        db = client.livraria
        resultado = db.editoras.find_one({
            '_id': ObjectId(editora_id)
        })
        
        if (resultado):
            edt = Editora(resultado['nome'], resultado['endereco'], resultado['telefone'])
            edt.id = resultado['id']
        
        client.close()

        return edt