"""Calcular o valor do juros compostos: Desenvolva uma função que calcula o valor final de 
um investimento com base em uma taxa de juros e um período de tempo.
Isso envolve a aplicação da fórmula de juros compostos."""

def juros_compostos(capital,taxa,tempo):
    montante = capital*((1+(taxa/100)))**tempo
    montante = round(montante,2)
    print(f"\nSeu montante foi de: {montante} R$")

print("\nO valor da taxa deve ser referente ao tempo dito, se taxa está em mês, o tempo deve ser em mêses.\n")
capital = float(input("\nDigite o valor do capital investido: "))
taxa = float(input("\nDigite o valor da taxa do investimento. "))
tempo = float(input("\nDigite o tempo que o capital estará investido: "))
juros_compostos(capital,taxa,tempo)