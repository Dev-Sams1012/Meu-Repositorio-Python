"""Calcular o fatorial de um número: Este exercício requer a criação de uma função que 
    calcula o fatorial de um número dado como entrada. 
    O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio número. """
    
def fatorial(valor):
    lista = []
    for termo in range(1,valor+1):
        lista.append(termo)
        
    resultado = lista[0]   
         
    for numero in range(1,len(lista)):
        resultado *= lista[numero]

    print(f"{valor}! = {resultado}.")

count = 1
while count == 1:
    valor = int(input("\nDigite o valor que deseja saber o fatorial: "))    
    fatorial(valor)
    count = int(input("\nDigite \"1\" para continuar ou qualquer outro número para parar.\n"))