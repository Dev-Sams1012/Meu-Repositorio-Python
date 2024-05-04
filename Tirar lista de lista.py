'''Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes'''

vetor = ["a","g","o","k","p","r","u","c","l","p"]
vogais = ["a","e","i","o","u"]

consoante = []
for elemento in vetor:
    if elemento not in vogais:
        consoante.append(elemento)
print(consoante)
