import database
import encryption


def envio_handler(usuario_logado):
    print("\n--- Enviar Nova Mensagem ---")

    destinatario = input("Para quem você quer enviar?: ").lower()
    senha = input("Digite a senha secreta combinada: ")
    mensagem = input("Digite sua mensagem: ")

    if not mensagem:
        print("\nVocê não pode enviar uma mensagem vazia.")
        return

    print("Criptografando mensagem...")
    try:
        conteudo_cifrado = encryption.criptografar(mensagem, senha)

        print("Salvando no banco de dados...")
        database.salvar_mensagem(usuario_logado, destinatario, conteudo_cifrado)

    except Exception as e:
        print(f"\nNão foi possível enviar a mensagem: {e}")


def leitura_handler(usuario_logado):
    print("\n--- Suas Novas Mensagens ---")

    mensagens_novas = database.buscar_mensagens_novas(usuario_logado)

    if not mensagens_novas:
        print("Você não tem nenhuma mensagem nova.")
        return

    qtd = len(mensagens_novas)
    if qtd == 1:
        print("Você tem 1 mensagem nova:")
    else:
        print(f"Você tem {qtd} mensagens novas:")



    for i, msg in enumerate(mensagens_novas):
        print(f"  {i+1}. De: {msg['remetente']} (ID: {msg['_id']})")

    try:
        escolha = int(input("\nQual mensagem deseja ler? (Digite o número): ")) - 1
        senha = input("Digite a senha secreta combinada: ")

        msg_escolhida = mensagens_novas[escolha]
        
        texto_original = encryption.descriptografar(msg_escolhida['conteudo_mensagem'], senha)
        
        if "Erro" in texto_original:
            print("\nSenha incorreta!")
        else:
            print(f"\n--- MENSAGEM ORIGINAL ---\nDe: {msg_escolhida['remetente']}\n")
            print(f'"{texto_original}"')
            
            database.marcar_mensagem_como_lida(msg_escolhida['_id'])
            
    except Exception as e:
        print(f"\nOpção inválida ou falha ao descriptografar: {e}")




def main():

    print(f"\nBem-Vindo ao Sistema De Mensagens! ")
    usuario = input("Digite seu nome ou @: ").lower()
    print(f"\nLogin feito como: {usuario}")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print(f"1 - Enviar uma mensagem.")
        print(f"2 - Ver minhas mensagens ")
        print(f"3- Sair")
        opcao = input("\nO que deseja fazer?: ")

        if (opcao == "1"):
            envio_handler(usuario)

        elif (opcao == "2"):
            leitura_handler(usuario)

        elif (opcao == "3"):
            print(f"Saindo... ")
            break
        else:
            print(f"Digite uma opcao valida!")

    
main()

    


