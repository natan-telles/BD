from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from prettytable import PrettyTable

def getURI():
    return "mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def inserirPaciente(id,nome,cpf,telefone):
    # Create - Inserir um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    db = client['hospital_rtm']
    collection = db['pacientes']
    document = {"_id":str(id),"nome":nome,"cpf": cpf,"telefone":telefone}
    collection.insert_one(document)
    print("Inserido com sucesso: ", document)

def mostraTodosPacientes():
    # Read - Encontrar documentos
    grid = PrettyTable(['id','nome','cpf','telefone'])

    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['pacientes']
    documentos = collection.find()

    for doc in documentos:
        #print(doc)  
        grid.add_row([doc['_id'],doc['nome'],doc['cpf'],doc['telefone']])

    grid.align = 'c'
    print(grid)
            
           
def mostraPaciente(id):
    # Read - Encontrar documentos
    grid = PrettyTable(['id','nome','cpf','telefone'])
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['pacientes']
    consulta = {"_id" : f"{id}"}
    documentos = collection.find(consulta)
    
    for doc in documentos:
        grid.add_row([doc['_id'],doc['nome'],doc['cpf'],doc['telefone']])
    grid.align = 'c'
    print(grid)    
            
def consultarPaciente(id):
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['pacientes']
    consulta = {"_id" : f"{id}"}
    documentos = collection.find(consulta)
    
    aux = 0
    for doc in documentos:
        aux+=1
        if aux > 0:
            break
    return aux

def alterarPaciente(id,novoNome,cpf,telefone):
    # Update - Atualizar um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['pacientes']
    consulta = {"_id": str(id)}
    novo_valor = {"$set": {"nome": novoNome,"cpf":cpf,"telefone":telefone}}
    collection.update_one(consulta, novo_valor)
    print("Registro alterado com sucesso!")

def deletarPaciente(id):
    # Delete - Remover um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['pacientes']
    consulta = {"_id": str(id)}
    collection.delete_one(consulta)