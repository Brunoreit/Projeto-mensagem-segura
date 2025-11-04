import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from bson.objectid import ObjectId

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    db = client['chat']
    mensagens_collection = db['mensageria']

except Exception as e:
    print(f"Erro ao selecionar coleção: {e}")


def salvar_mensagem(remetente, destinatario, mensagem_cifrada):
    try:
        mensagens_collection.insert_one(
            {
                "remetente": remetente,
                "destinatario": destinatario,
                "conteudo_mensagem": mensagem_cifrada,
                "status": "nova",
                "timestamp": datetime.now()
            }
        )
        print(f"Mensagem salva no banco de dados.")

    except Exception as e:
        print(f"Falha ao salvar mensagem no banco: {e}")    


def buscar_mensagens_novas(nome_user):
    try:
        resultado = mensagens_collection.find({
            "destinatario": nome_user,
            "status": "nova"
        })

        return list(resultado)
    
    except Exception as e:
        print(f"Falha ao buscar mensagens: {e}")
        return[]
    


def marcar_mensagem_como_lida(ID_mensagem):
    try:
        mensagens_collection.update_one(
            {"_id": ObjectId(ID_mensagem)},
            {"$set": {"status": "lida"}}
        )
        print(f"Mensagem marcada como lida.")

    except Exception as e:
        print(f"Falha ao atualizar status da mensagem {e}")