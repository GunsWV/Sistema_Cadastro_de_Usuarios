# Função para separar visualmente
def mostra_linha():
    print('-' * 50)

# Lista inicial (pode começar vazia também)
nomes = []

print("=== GERENCIADOR DE NOMES ===")

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar nome")
    print("2 - Listar nomes")
    print("3 - Editar nome")
    print("4 - Remover nome")
    print("5 - Limpar lista")
    print("6 - Sair")

    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    match opcao:

        # Adicionar nome
        case 1:
            nome = input("Digite o nome: ").strip()
            if nome:
                nomes.append(nome)
                print(f"{nome} adicionado com sucesso!")
            else:
                print("Nome inválido.")
            mostra_linha()

        # Listar nomes
        case 2:
            if not nomes:
                print("A lista está vazia.")
            else:
                print("Lista de nomes:")
                for i, nome in enumerate(nomes):
                    print(f"{i} - {nome}")
            mostra_linha()

        # Editar nome
        case 3:
            if not nomes:
                print("Lista vazia.")
            else:
                for i, nome in enumerate(nomes):
                    print(f"{i} - {nome}")

                try:
                    indice = int(input("Digite o índice para editar: "))
                    if 0 <= indice < len(nomes):
                        novo_nome = input("Digite o novo nome: ").strip()
                        if novo_nome:
                            nomes[indice] = novo_nome
                            print("Nome atualizado com sucesso!")
                        else:
                            print("Nome inválido.")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Digite um número válido.")
            mostra_linha()

        # Remover nome
        case 4:
            if not nomes:
                print("Lista vazia.")
            else:
                for i, nome in enumerate(nomes):
                    print(f"{i} - {nome}")

                try:
                    indice = int(input("Digite o índice para remover: "))
                    if 0 <= indice < len(nomes):
                        removido = nomes.pop(indice)
                        print(f"{removido} removido com sucesso!")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Digite um número válido.")
            mostra_linha()

        # Limpar lista
        case 5:
            nomes.clear()
            print("Lista apagada com sucesso.")
            mostra_linha()

        # Sair
        case 6:
            print("Encerrando o programa...")
            break

        # Opção inválida
        case _:
            print("Opção inválida.")
            mostra_linha()