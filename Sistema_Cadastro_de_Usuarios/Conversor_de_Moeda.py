# Constante da taxa de câmbio (dólar para real)
DOLAR = 5.71

# Função para converter dólar para real
def converter_para_real(valor_em_dolar):
    return valor_em_dolar * DOLAR

# Função principal
def main():
    print("=== CONVERSOR DE MOEDA (USD → BRL) ===")

    while True:
        try:
            # Entrada do usuário
            valor_em_dolar = float(input("Digite o valor em dólares: "))

            # Validação
            if valor_em_dolar < 0:
                print("Digite um valor positivo.")
                continue

            # Conversão
            valor_em_real = converter_para_real(valor_em_dolar)

            # Saída formatada
            print(f"Valor em reais: R$ {valor_em_real:.2f}")

        except ValueError:
            print("Digite um número válido.")

        # Pergunta se quer continuar
        continuar = input("Deseja converter outro valor? (s/n): ").lower()

        if continuar != 's':
            print("Encerrando o programa...")
            break


# Executa o programa
main()