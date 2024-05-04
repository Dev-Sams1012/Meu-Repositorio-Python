"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que
a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

count = 1
while count == 1:
    pais_A = float(input("\nQual a população do Pais A? "))
    pais_B = float(input("\nQual a população do Pais B? "))
    anos_passados = 0
    taxa_A =  (float(input("\nQual a taxa de aumento do Pais A? ")))/100
    taxa_B =  (float(input("\nQual a taxa de aumento do Pais B? ")))/100
    
    while pais_A <= pais_B:
        pais_A += pais_A * taxa_A
        pais_B += pais_B * taxa_B
        anos_passados += 1    
    pais_A = round(pais_A)
    pais_B = round(pais_B)    
    print(f"{anos_passados} anos\nA população do País A é: {pais_A},\nA população do País B é: {pais_B}.")
    count = int(input("\nDigite 1 para continuar ou qualquer outro número para parar.\nDeseja realizar outra simulação? "))