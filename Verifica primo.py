'''Verificar se um número é primo: Implemente um programa que verifique 
se um número é primo, ou seja, se é divisível apenas por 1 e por ele mesmo.'''

def verifica_primo(valor):
    count = 0
    for i in range(2,valor):
        if valor % i == 0: 
            count += 1
    if count >= 1 or valor <= 1:
        print(f"{valor} não é primo. ele é divísivel por {count} números além do \"1\".")
    else:
        print(f"{valor} é primo.")
        
    
meu_valor = int(input("\nDigite um número para saber se é primo ou não: "))        
verifica_primo(meu_valor)