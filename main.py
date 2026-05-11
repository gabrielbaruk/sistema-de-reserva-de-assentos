while True:
    print("Sistema de Reserva de Assentos")

    print("1. Usuários")
    print("2. Assentos")
    print("3. Sair")

    opcao = (input("Escolha umas da opções: "))

    if opcao == "1":
        print("Usuários")
    elif opcao == "2":
        print("Assentos")
    elif opcao == "3":
        break
    else:
        print("Opcão inválida")

print("O programa foi encerrado")