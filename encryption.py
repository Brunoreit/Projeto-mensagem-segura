from simplecrypt import encrypt, decrypt
# Funcao de Criptografia

def criptografar(mensagem,senha):
    criptografado = encrypt(mensagem,senha)
    return criptografado

#Funcao de Descriptografia
def descriptografar(original,senha):
    try:
        original = decrypt(senha,original).decode()
        return original
    except:
        return "Erro: Senha incorreta!"
