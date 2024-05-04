"""Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem."""

def Potencia(base,expoente):
    resultado = 1
    for i in range(0,expoente):
        resultado *= base
    print(f"\n{resultado}")

count = 1
while count == 1:
    base = int(input("\nDigite um valor para a base da potência: "))
    potencia = int(input("\nDigite o valor para o expoente da potência: "))
    Potencia(base,potencia)
    count = int(input("\nDigite 1 para repetir ou qualquer outro valor para parar: "))