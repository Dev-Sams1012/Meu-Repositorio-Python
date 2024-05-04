# Valor de entrada, que será modificado ao final.
entrada = input("Escreva aqui a instrução: ")

# Conversão do valor de entrada numa lista, para facilitar os procedimentos.
lista = list(entrada)

# Função utilizada para ter o valor do tamanho da lista.
i = len(lista) 

# Criação de uma varíavel que será usada para comparar um index da lista com o seu próximo.
indice = 0  

""" Pocedimento de repetição, que irá funcionar ENQUANTO o valor que será feito a comparação
seja menor que o último a ser contado ( se fosse apenas "i", iria considerar o próximo,
que não está na lista.)"""
while indice < i - 1: 
    if lista[indice] == lista[indice+1]: # Comparação se o index X é igual ao próximo ( X + 1 ).
        lista.pop(indice+1) # Caso for igual, irá EXPLODIR o ( X + 1 ), deixando ainda o valor X.
        i -= 1 # Considerar que já que um termo "explodiu", a lista diminuiu um termo.
    else:
        indice += 1 # Se caso X for diferente de ( X + 1 ), irá pular um índice, ou seja, comparar logo
                    # ( X + 1 ) com ( X + 2 ).
                    
resultado = "".join(lista) # Já que queremos o resultado em string, JUNTEI os termos da lista.
    
print(resultado) # Como se é esperado... Ao final, o resultado é mostrado.