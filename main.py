import os


opcao = 0
usuarios = []
assentos = []
reservas = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_title():
    print('''
 ____  _     _                             _      
/ ___|(_)___| |_ ___ _ __ ___   __ _    __| | ___ 
\___ \| / __| __/ _ \ '_ ` _ \ / _` |  / _` |/ _ \
 ___) | \__ \ ||  __/ | | | | | (_| | | (_| |  __/
|____/|_|___/\__\___|_| |_| |_|\__,_|  \__,_|\___|
|  _ \ ___  ___  ___ _ ____   ____ _    __| | ___ 
| |_) / _ \/ __|/ _ \ '__\ \ / / _` |  / _` |/ _ \
|  _ <  __/\__ \  __/ |   \ V / (_| | | (_| |  __/
|_| \_\___||___/\___|_|    \_/ \__,_|  \__,_|\___|
   / \   ___ ___  ___ _ __ | |_ ___  ___          
  / _ \ / __/ __|/ _ \ '_ \| __/ _ \/ __|         
 / ___ \\__ \__ \  __/ | | | || (_) \__ \         
/_/   \_\___/___/\___|_| |_|\__\___/|___/      
        
    ''')

def show_menu(menu):
    global opcao
    clear_screen()
    if(menu == "principal"):
        print("1. Ver mapa")
        print("2. Reservar assento")
        print("0. Voltar")
    opcao = (input("Escolha umas da opções: "))
    
while True:
    print("Sistema de Reserva de Assentos")

    print("1. Usuários")
    print("2. Assentos")
    print("3. Reserva")
    print("0. Sair")

    if opcao == "1":
        clear_screen()
        print ("Usuário")
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
        clear_screen()
        print("1. Assentos")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Mostrar mapa")
    elif opcao == "3":
        clear_screen()
        print("1. Reservar Assento")
        print("2. Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Reservando assento")
        elif opcao == "2":
            print("Voltar ao menu") 
    elif opcao == "0":
        clear_screen()
        print("Saindo do sistema...")
        break
    else:
        print("Opcão inválida")

print("O programa foi encerrado")