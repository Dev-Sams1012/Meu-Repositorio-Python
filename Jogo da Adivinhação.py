"""16) Faça um programa que escolha um número aleatório entre 1 e 10 e peça
para o usuário adivinhá-lo. Antes de iniciar o jogo, escreva no terminal a
tela abaixo:
Adivinhe o número! Escolha o nível:
1 - Fácil
2 - Difícil
3 - Insano
Digite a sua opção:
● O nível Fácil permite quantas tentativas forem necessárias para o
usuário acertar o número e mostra dicas quando ele errar: Tente um
número maior! (se o usuário digitou um número menor do que o
escolhido) ou Tente um número menor! (se o usuário digitou um
número maior do que o escolhido).
● O nível Difícil limita o número de tentativas em 3, ainda mostrando as
dicas.
● O nível Insano também limita o número de tentativas em 3, mas sem
dicas.
Ao final diga em quantas tentativas o usuário acertou o número. Utilize o
código abaixo para gerar o número aleatório:"""

import random as rd

aleatorio = rd.randint(1,30)
resume = "s"

nivel = int(input("Adivinhe o número! Escolha o nível: "))
while resume == "s":
    tentativas = 9
    if nivel == 1:
        numero = int(input("Escolha um número: "))
        if numero == aleatorio:
            resume = input("digite \"s\" para continuar: ")
            aleatorio = rd.randint(1,30)
            nivel = int(input("Adivinhe o número! Escolha o nível: "))
        else:
            if numero > aleatorio:
                print("tente um numero menor")
            else:
                print("tente um numero maior")
    elif nivel == 2:
        while tentativas > 0:
            numero = int(input("Escolha um número: "))
            if numero == aleatorio:
                resume = input("digite \"s\" para continuar: ")
                aleatorio = rd.randint(1,30)
                nivel = int(input("Adivinhe o número! Escolha o nível: "))
            else:
                if numero > aleatorio:
                    print("tente um numero menor")
                else:
                    print("tente um numero maior")
                print(f"você tem {tentativas} tentativas.")
                tentativas -= 1