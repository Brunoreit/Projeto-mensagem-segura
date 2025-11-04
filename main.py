import os
import pymongo
from pymongo import MongoClient
from funcoes import criptografar,descriptografar




print(f"Bem-Vindo ao Sistema De Mensagem ")
usuario = input("Digite seu nome ou @: ")
print(f"1 - Enviar uma mensagem.")
print(f"2- Ver minhas mensagens ")
print(f"3- Sair")
opcao = input("O que deseja fazer? ")
if (opcao == 1):
    print(f"A mensagem precisa ter no minimo 50 caracteres")
    senha = input("Digite a senha combinada: ")
    mensagem = input("Digite sua mensagem: ")
    if mensagem.length<50:
        print(f"Minimo de 50 caracteres nao atingido!")
    else:    
        criptografar(mensagem,senha)

elif (opcao == 2):
    print("Mostrando suas novas mensagens!")
    try: 
        uri = os.getenv("MONGODB_URI")
        client = MongoClient(uri)
        database = client["projeto-mensagem"]
        collection = database["nome da colecao"]
        results = collection.find({ "STATUS" : "NOVA MENSAGEM" })
        for document in results:
            print(document)
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
elif (opcao == 3):
    print(f"Saindo... ")
    exit()
else:
    print(f"Digite uma opcao valida!")

    


