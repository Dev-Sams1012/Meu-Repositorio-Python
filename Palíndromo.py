"""Verificar se uma palavra é um palíndromo: Implemente um programa que verifica se uma palavra é um 
palíndromo. Um palíndromo é uma palavra que pode ser lida da mesma forma tanto da 
esquerda para a direita quanto da direita para a esquerda."""

def palindromo(palavra):
    oposto = palavra[::-1]
    
    if palavra == oposto:
        print(f"\nA palavra {palavra} é um palíndromo")
    else:
        print(f"\na palavra {palavra} não é um palíndromo, {palavra} e {oposto} são palavras diferentes.")

palavra = input("Escreva uma palavra para saber se ela é um palíndromo: ")

palindromo(palavra)