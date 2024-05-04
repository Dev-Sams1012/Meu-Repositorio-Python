'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR
e os números IMPARES no vetor impar. Imprima os três vetores.'''

vetor = []
pares = []
impares = []
def Par_ou_Impar(vetor):
    for elementos in vetor:
        if elementos%2 == 0:
            pares.append(elementos)
        else:
            impares.append(elementos)

    print(f"\nA lista original é: {vetor}\n")
    print(f"Os pares são: {pares}\n")
    print(f"Os ímpares são: {impares}\n")

count = 1
for count in range(20):
    x = int(input("Escreva um número: "))
    vetor.append(x)
    count += 1
    
Par_ou_Impar(vetor)