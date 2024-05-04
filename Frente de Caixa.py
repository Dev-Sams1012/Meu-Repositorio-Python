"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui 
uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto 
inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:"""

"""Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00"""

def frente_de_caixa():
    i = 1
    valor = 1
    total_da_compra = []
    
    while valor != 0:
           valor = float(input("\nDigite o valor do produto: "))
           if valor == 0:
               continue
           quantidade = int(input("\nDigite a quantidade do produto: "))
           valor_total = valor * quantidade
           print(f"produto {i}: R$ {valor} * {quantidade} -> R$ {valor_total}")
           total_da_compra.append(valor_total)
           i += 1
           
    total = sum(total_da_compra)
    print(f"\nTotal: R$ {total}")
    
    dinheiro = float(input("Dinheiro:  "))
    troco = dinheiro - total
    
    while troco < 0:
        print("\nVocê não pagou tudo.")
        dinheiro = float(input("Dinheiro:  "))
        troco = dinheiro - total
        
    troco = round(troco,2)
    print(f"\nTroco: R$ {troco}")
#------------------------------------------#
j = 1
while j == 1:
    frente_de_caixa()
    j = int(input("\nDigite 1 para próxima compra ou qualquer outro número para parar: "))
