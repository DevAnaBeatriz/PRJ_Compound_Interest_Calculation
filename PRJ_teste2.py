def calcular_parcelas(valor_financiamento, num_parcelas):
    # Tabela de taxas de juros anuais
    tabela_juros = {
        (0, 6): 0.07, #7% de juros
        (7, 12): 0.10, #10% de juros
        (13, 18): 0.12, #12% de juros
        (19, 24): 0.15, #15% de juros
        (25, float('inf')): 0.18 #18% de juros
    }

    # Encontrando a taxa de juros anual correspondente ao número de meses
    for faixa, taxa in tabela_juros.items():
        if faixa[0] <= num_parcelas <= faixa[1]:
            taxa_juros_anual = taxa
            break

    # Taxa de juros mensal
    taxa_juros_mensal = taxa_juros_anual / 12

    # Calculando o valor da parcela usando a fórmula de juros compostos
    valor_parcela = valor_financiamento * (taxa_juros_mensal * (1 + taxa_juros_mensal)**num_parcelas) / ((1 + taxa_juros_mensal)**num_parcelas - 1)

    # Calculando o valor total com juros
    valor_total_com_juros = valor_parcela * num_parcelas

    # Calculando o valor total dos juros
    valor_total_juros = valor_total_com_juros - valor_financiamento

    # Exibindo resultados
    print(f"Valor da parcela: R${valor_parcela:.2f}")
    print(f"Valor total com juros: R${valor_total_com_juros:.2f}")
    print(f"Valor total dos juros: R${valor_total_juros:.2f}")

if __name__ == "__main__":
    # Verificar e obter o valor do financiamento
    while True:
        try:
            valor_financiamento = float(input("Informe o valor do financiamento: R$"))
            break
        except ValueError:
            print("Por favor, insira um valor válido.")

    # Verificar e obter o número de parcelas
    while True:
        try:
            num_parcelas = int(input("Informe o número de parcelas: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    # Chamar a função para calcular parcelas e exibir resultados
    calcular_parcelas(valor_financiamento, num_parcelas)
