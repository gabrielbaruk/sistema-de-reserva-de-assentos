while True:
    print("Sistema de Reserva de Assentos")

    print("1. Usuários")
    print("2. Assentos")
    print("3. Sair")

    opcao = (input("Escolha umas da opções: "))

    if opcao == "1":
        print("1. Usuários")
        print("2. Ver usuário")
        print("3. Verificar")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Cadastrar usuário")
            Digite_um_nome = input("Digite seu nome: ")
        elif opcao == "2":
            print("Listar Usuário")
        elif opcao == "3":
            print("Verificar usuário")
            Faça_uma_verificação = input("Resolva O ReCaptcha")
        else:
            print("Opção inválida. Por favor tente novamente")
            continue
    elif opcao == "2":
        print("1. Assentos")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Mostrar mapa")
            Digite_seu_assento = input("Qual seu assento? ")
            print("Mostrar assento")
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opcão inválida")

print("O programa foi encerrado")