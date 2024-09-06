from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from prettytable import PrettyTable

def getURI():
    return "mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def isPaciente(nomePaciente):
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['pacientes']
    consulta = {"nome" : f"{nomePaciente}"}
    documentos = collection.find(consulta)
    
    aux = 0
    for doc in documentos:
        aux+=1
        if aux > 0:
            break
    
    if aux == 0:
        return False
    else:
        return True

def isMedico(nomeMedico):
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['medicos']
    consulta = {"nome" : f"{nomeMedico}"}
    documentos = collection.find(consulta)
    
    aux = 0
    for doc in documentos:
        aux+=1
        if aux > 0:
            break
    
    if aux == 0:
        return False
    else:
        return True

def inserirConsulta(id,nomePaciente,nomeMedico,data,hora):
    # Create - Inserir um documento
    if(isPaciente(nomePaciente) and isMedico(nomeMedico)):
        uri = getURI()
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        db = client['hospital_rtm']
        collection = db['consultas']
        document = {"_id":str(id),"nome_paciente":nomePaciente,"nome_medico": nomeMedico,"data":data,"hora":hora}
        collection.insert_one(document)
        print("Consulta inserida com sucesso: ", document)
    else:
        print("Médico ou paciente inseridos não cadastrados! Por Favor cadastre-os primeiro antes de agendar consulta.")

def mostraTodasConsultas():
    # Read - Encontrar documentos
    grid = PrettyTable(['id','nome_paciente','nome_medico','data','hora'])

    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['consultas']
    documentos = collection.find()
    total = 0
    for doc in documentos:
        grid.add_row([doc['_id'],doc['nome_paciente'],doc['nome_medico'],doc['data'],doc['hora']])
        total+=1

    if total == 0:
        print("Não existem consultas cadastradas!")
    else:
        grid.align = 'c'
        print(grid)
            
           
def mostraConsulta(id):
    # Read - Encontrar documentos
    grid = PrettyTable(['id','nome_paciente','nome_medico','data','hora'])

    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['consultas']
    consulta = {"_id" : f"{id}"}
    documentos = collection.find(consulta)
    for doc in documentos:
       grid.add_row([doc['_id'],doc['nome_paciente'],doc['nome_medico'],doc['data'],doc['hora']]) 
    
    grid.align = 'c'
    print(grid)
            
def consultarConsulta(id):
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['consultas']
    consulta = {"_id" : f"{id}"}
    documentos = collection.find(consulta)
    
    aux = 0
    for doc in documentos:
        aux+=1
        if aux > 0:
            break
    return aux

def alterarConsulta(id,nomePaciente,nomeMedico,data,hora):
    # Update - Atualizar um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['consultas']
    consulta = {"_id": str(id)}
    novo_valor = {"$set": {"nome_paciente": nomePaciente,"nome_medico":nomeMedico,"data":data,"hora":hora}}
    collection.update_one(consulta, novo_valor)
    print("Consulta alterada com sucesso!")

def deletarConsulta(id):
    # Delete - Remover um documento
    uri = getURI()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['hospital_rtm']
    collection = db['consultas']
    consulta = {"_id": str(id)}
    collection.delete_one(consulta)