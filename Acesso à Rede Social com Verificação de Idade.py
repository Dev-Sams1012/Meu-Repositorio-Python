### Parte 1 ###

# Foi usando do 1 ao 6 pois quis que aparecesse ao primeiro usuário um ID "1", não "0".
for i in range(1,6):
    tentativas = 2 # Foi colocado 2 tentativas pois ao considerar o "0", ficam 3 tentativas!
    usuario = int(input(f"\nUsuário {i}, digite sua idade: "))
    if usuario >= 18: # Verificação da maioridade de idade do usuário em específico.
        print("Você é maior de idade. Pode tentar acessar a rede social.")
        
        ### Parte 2 ###
        while tentativas >= 0: # Enquanto houver tentativas restantes, a repetição poderá ocorrer.
            senha = input("Digite a senha: ")
            if senha == "senha123": # Verificação da senha de acesso
                print("Acesso permitido.")
                break # Foi usado o "break" para dar continuidade ao próximo usuário (i++).
            else:
                print(f"Senha incorreta. Você tem mais {tentativas} tentativa(s)")
                tentativas -= 1 # Por ser usado um laço "While", é interessante usar um "Contador" para marcar as "voltas".
                
    elif usuario < 18 and usuario > 0:
        print("Você não é maior de idade. Acesso não permitido") # Caso o usuário inserir que tem idade menor que 18 anos.
    else:
        print("Idade inválida") # Caso o usuário colocar uma idade negativa ou igual a 0 ( absurdo )

    