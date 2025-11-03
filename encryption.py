from cryptography.fernet import Fernet

# Cria um chave
chave = Fernet.generate_key()
cipher = Fernet(chave)

# Funcao de Criptografia
def criptografar():
    mensagem = input("Envie sua mensagem: ").encode()
    criptografado = cipher.encrypt(mensagem)
    print(f"Criptografado: {criptografado}")

#Funcao de Descriptografia
def descriptografar():
    original = cipher.decrypt(criptografado) 
    print(f"Descriptografado: {original.decode()}")
