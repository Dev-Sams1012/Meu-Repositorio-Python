""" Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e 
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado."""

'''Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!'''

import random as ra

x = open("Testes/teste.txt", "r")

def aleatorias():
    lista = []
    linhas = x.readlines()
    for i in linhas:
        i = i.replace("\n", "")
        i = i.lower()
        lista.append(i)

    aleatorio = ra.choice(lista)

    return aleatorio

def mostrar_palavra(palavra,letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += '_ '
    return resultado.strip()

def jogo_da_forca():
    palavra = aleatorias()
    letras_corretas = []
    tentativas = 6
    
    while tentativas > 0:
        palavra_mostrada = mostrar_palavra(palavra, letras_corretas)
        print(f'Palavra: {palavra_mostrada}')
        print(f'Tentativas restantes: {tentativas}')
        
        letra = input("Escreva uma letra: ")
        letra = letra.lower()
        
        if letra in letras_corretas:
            print("você já escolheu essa letra!")
        elif letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Você errou.")
            
        if "_" not in mostrar_palavra(palavra, letras_corretas):
            print("Parabéns!")
            break
    
    if tentativas == 0:
        print("Perdeu.")
        
        
jogo_da_forca()    
x.close()