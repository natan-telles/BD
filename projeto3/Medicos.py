from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from prettytable import PrettyTable

#Formato do CRM -> composto por seis números + a sigla CRM acompanhada do estado, exemplo: 12345/SP

def getURI():
    return "mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def inserirMedico(id,nome,CRM,especialidade):
    # Create - Inserir um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    db = client['hospital_rtm']
    collection = db['medicos']
    document = {"_id":str(id),"nome":nome,"crm": CRM,"especialidade":especialidade}
    collection.insert_one(document)
    print("Inserido com sucesso: ", document)

def mostraTodosMedicos():
    # Read - Encontrar documentos
    grid = PrettyTable(['id','nome','CRM','especialidade'])

    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['medicos']
    documentos = collection.find()
    total = 0
    for doc in documentos:
        total+=1
        grid.add_row([doc['_id'],doc['nome'],doc['crm'],doc['especialidade']])

    if total == 0:
        print("Não existem médicos cadastrados!")
    else:
        grid.align = 'c'
        print(grid)
            
           
def mostraMedico(id):
    # Read - Encontrar documentos
    grid = PrettyTable(['id','nome','CRM','especialidade'])

    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['medicos']
    consulta = {"_id" : f"{id}"}
    documentos = collection.find(consulta)

    for doc in documentos:
        grid.add_row([doc['_id'],doc['nome'],doc['crm'],doc['especialidade']])

    grid.align = 'c'
    print(grid)
            
            
def consultarMedico(id):
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['medicos']
    consulta = {"_id" : f"{id}"}
    documentos = collection.find(consulta)
    
    aux = 0
    for doc in documentos:
        aux+=1
        if aux > 0:
            break
    return aux

def alterarMedico(id,nome,CRM,especialidade):
    # Update - Atualizar um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['medicos']
    consulta = {"_id": str(id)}
    novo_valor = {"$set": {"nome": nome,"crm":CRM,"especialidade":especialidade}}
    collection.update_one(consulta, novo_valor)
    print("Registro alterado com sucesso!")

def deletarMedico(id):
    # Delete - Remover um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['medicos']
    consulta = {"_id": str(id)}
    collection.delete_one(consulta)