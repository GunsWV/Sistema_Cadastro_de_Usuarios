# Função para mostrar uma linha separadora no terminal
def mostra_linha():
    print('-' * 50)  # imprime 50 traços

# Lista que vai armazenar os nomes dos usuários
lista_de_nomes = []

# Mensagem inicial do sistema
print("Olá, seja bem-vindo à central de cadastro da FABPROG!")

# Loop infinito (o programa só para quando escolher sair)
while True:

    # Exibe o menu de opções
    print("\nO que você deseja fazer?")
    print("1 - Cadastrar usuário")
    print("2 - Remover usuário")
    print("3 - Listar usuários")
    print("4 - Sair")

    # Tratamento de erro caso o usuário digite algo que não seja número
    try:
        codigo = int(input("Digite uma opção: "))  # converte a entrada para número
    except ValueError:
        print("Por favor, digite um número válido.")  # mensagem de erro
        continue  # volta para o início do loop

    # Estrutura de decisão baseada na opção escolhida
    match codigo:

        # Opção 1: cadastrar usuário
        case 1:
            nome_usuario = input("Digite o nome para cadastro: ").strip()  # remove espaços extras

            if nome_usuario:  # verifica se o nome não está vazio
                lista_de_nomes.append(nome_usuario)  # adiciona o nome na lista
                print(f"{nome_usuario} foi cadastrado com sucesso!")
            else:
                print("Nome inválido.")  # caso o usuário não digite nada

            mostra_linha()  # linha separadora

        # Opção 2: remover usuário
        case 2:
            nome_remover = input("Digite o nome a ser removido: ").strip()

            # verifica se o nome existe na lista
            if nome_remover in lista_de_nomes:
                lista_de_nomes.remove(nome_remover)  # remove o nome
                print(f"{nome_remover} foi removido com sucesso!")
            else:
                print("Nome não encontrado.")  # evita erro caso não exista

            mostra_linha()

        # Opção 3: listar usuários
        case 3:
            # verifica se a lista está vazia
            if not lista_de_nomes:
                print("Nenhum usuário cadastrado.")
            else:
                print("Usuários cadastrados:")

                # percorre a lista e mostra cada nome
                for nome in lista_de_nomes:
                    print(f"- {nome}")

            mostra_linha()

        # Opção 4: sair do programa
        case 4:
            print("Encerrando o programa...")
            break  # encerra o loop

        # Caso o usuário digite uma opção inválida
        case _:
            print("Opção inválida. Tente novamente.")
            mostra_linha()