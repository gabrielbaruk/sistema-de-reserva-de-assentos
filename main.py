import os
import uuid

usuarios = []
reservas = []


linhas, colunas = 5, 5
mapa_assentos = [["0" for _ in range(colunas)]for _ in range(linhas)]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pressione_enter():
    print("-" + "-" * 30)
    input('Pressione ENTER para continuar...')


def show_title():
    print(
        '''
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
        
    '''
    )

def exibir_mapa_visual():
    print("========= PALCO / TELA =========")
    print("\n " + " - ".join([f"C{c}" for c in range(colunas)]))
    for i, linha in enumerate(mapa_assentos):
        print(f"L{i} | " + "   ".join(linha) + " |")
        print("=========================\n")


def verificar_assento_ocupado(l, c):
    if mapa_assentos[l][c] == "X":
        return True
    return False


while True:
    clear_screen()
    show_title()


    print("====== MENU PRINCIPAL =======")
    print("1. Usuários")
    print("2. Assentos")
    print("3. Reserva")
    print("0. Sair")

    opcao = input("Escolha umas da opções: ")

    if opcao == "1":
        while True:
            clear_screen()
            print ("==== Usuário ====")
            print("1. Cadastrar usuário")
            print("2. Ver usuários")
            print("0. Voltar ao menu")
            print("=========================")
            sub_opcao = input("Escolha: ")

            if sub_opcao == "1": 
                Digite_um_nome = input("\nDigite seu nome: ").strip()
                if Digite_um_nome:

                    user_id = str(uuid.uuid4())[:6]
                    usuarios.append({"id": user_id, "nome": Digite_um_nome})
                    print(
                        f"Usuário '{Digite_um_nome}' cadastrado com sucesso! (ID: {user_id})"
                    )
                else:
                    print("Nome Inválido.")
                pressione_enter()

            elif sub_opcao == "2":
                print("==== Lista de Usuários ====")
                if not usuarios:
                    print("Nenhum usuário cadastrado")
                for u in usuarios:
                    print(f"ID: {u["id"]} | Nome: {u["nome"]}")
                pressione_enter()

            elif sub_opcao == "0":
                break
            else:
                print("Opcão inválida.")
                pressione_enter()

    elif opcao == "2":
        clear_screen()
        print("==== MAPA DE RESERVAS ====")
        exibir_mapa_visual()
        print("Legenda: O = Livre | X = Reservado")
        pressione_enter()

    elif opcao == "3":
        while True:
            clear_screen()
            print("==== SUBMENU DE RESERVAS ====")
            print("1. Realizar nova reserva")
            print("2. Listar histórico de reservas")
            print("0. Voltar ao menu principal")
            print("==================")
            sub_opcao = input("Escolha: ")
            
            if sub_opcao == "1": 
                if not usuarios:
                    print(
                        "Erro: Por favor cadastre um usuário antes de reservar."
                    )
                    pressione_enter()
                    continue

                print("--- Usuários Disponíveis ---")
                for idx, u in enumerate(usuarios):
                    print(f"[{idx}] - {u["Digite um nome"]} (ID: {u["id"]})")

                try:
                    num_user = int(
                        input("Selecione o número do usuário:")
                    )
                    usuario_selecionado = usuarios[num_user]

                    exibir_mapa_visual()

                    L = int(input(f"Digite a linha (0 a {linhas-1}): "))
                    C = int(
                        input(f"Digite a coluna (0 a {colunas-1}): ")
                        )
                    if 0 <= 1 <linhas and 0 <= C < colunas:
                        if verificar_assento_ocupado(1, C):
                            print(
                                f"O assento [Linha {1}, Coluna {C} Já está reservado!"
                            )
                        else:
                            mapa_assentos[1][C] = "X"
                            nova_reserva = {
                                "usuário": usuario_selecionado["nome"],
                                "assento": f"Linha {L}" f"Coluna {C}",
                            }
                            reservas.append(nova_reserva)
                            print(
                                f"Assento reservado para {usuario_selecionado["nome"]}."
                            )
                    else:
                        print("Posição inválida")

                except(ValueError, IndexError):
                    print("Entrada inválida, por favor digite o número correto.")

                pressione_enter()

            elif sub_opcao == "2":
                print("\n==== Histórico de reservas ====")
                if not reservas:
                    print("Nenhuma reserva no momento")
                for r in reservas:
                    print(f"{r["usuário"]} -> {r["assento"]}")
                pressione_enter()

            elif sub_opcao == "0":
                clear_screen()
                print("Saindo do sistema...")
                break

    else:
        print("Opçao Inválida tente novamente")
        pressione_enter()

    print("O programa foi encerrado")