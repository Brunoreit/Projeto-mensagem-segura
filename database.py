import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

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