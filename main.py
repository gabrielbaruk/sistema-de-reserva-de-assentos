


opcao = 0
usuarios = []
assentos = []
reservas = []


def clear_screen():
    os.system(cls if os.name == "nt" else "clear")

while True:
    print("Sistema de Reserva de Assentos")

    print("1. Usuários")
    print("2. Assentos")
    print("3. Reserva")
    print("4. Sair")

    opcao = (input("Escolha umas da opções: "))

    if opcao == "1":
        clear_screen
        print("1. Usuários")
        print("2. Ver usuário")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Cadastrar usuário")
            Digite_um_nome = input("Digite seu nome: ")
        elif opcao == "2":
            print("Listar Usuário")
        else:
            print("Opção inválida. Por favor tente novamente")
            continue
    elif opcao == "2":
        clear_screen
        print("1. Assentos")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Mostrar mapa")
    elif opcao == "3":
        clear_screen
        print("1. Reservar Assento")
        print("2. Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Reservando assento")
        elif opcao == "2":
            print("Voltar ao menu") 
    elif opcao == "4":
        clear_screen
        print("Saindo do sistema...")
        break
    else:
        print("Opcão inválida")

print("O programa foi encerrado")