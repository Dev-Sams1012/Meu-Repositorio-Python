'''Construa uma função que receba uma string como parâmetro e 
devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer 
outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres 
serão devolvidos em caixa alta ou caixa baixa,independentemente de como foram digitados.'''

import random

def embaralhar(palavra):
    palavra_maiuscula = palavra.upper()
    palavra_separada = []
    palavra_separada = list(palavra_maiuscula)
    random.shuffle(palavra_separada)
    separador = ""
    palavra_embaralhada = separador.join(palavra_separada)
    print(palavra_embaralhada)
    
palavra = input("Escreva uma palavra para ser embaralhada: ")
embaralhar(palavra)