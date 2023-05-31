from pymongo import MongoClient
from pymongo.server_api import ServerApi

class ClientFactory:
    
    def get_client(self):
        return MongoClient("mongodb+srv://olivebri:sa3RY8vAWn5g6g6w@cluster0.jovjuzl.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

