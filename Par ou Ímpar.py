def Par_ou_Ímpar(number):
    if number%2 == 0:
        print(f"{number} é par.")
    else:
        print(f"{number} é ímpar.")
        
count = 1
while count == 1:
    number = int(input("Escolha um númmero para saber se é par ou ímpar: "))
    Par_ou_Ímpar(number)
    count = int(input(f"Digite \"1\" para continuar ou qualquer outro número para parar. "))