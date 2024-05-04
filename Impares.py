# Faça um programa, utilizando for, que peça para o usuário inserir um número N e mostre na tela todos os números ímpares até N.

limite = int(input("Até qual número você quer saber os ímpares? "))
for numero in range(limite):
    if numero % 2 != 0:
        print(numero)