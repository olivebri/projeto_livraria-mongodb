from pymongo import MongoClient
from pymongo.server_api import ServerApi

class ClientFactory:
    
    def get_client(self):
        return MongoClient("mongodb+srv://<user>:<password>@cluster0.jovjuzl.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

