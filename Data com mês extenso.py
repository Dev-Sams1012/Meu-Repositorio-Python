"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida."""

Mes = [(), "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
        "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def data_extenso(data):
    data = data.split('/')
    data_int = []
    for termo in data:
        data_int.append(int(termo))
    
    dia = data_int[0]
    if dia < 1 or dia > 31:
        print("Dia Inválido.")
        
    mes = data_int[1]
    if mes < 1 or mes > 12:
        print("Mês Inválido.")
    elif mes == 2 and dia > 29:
        print("Fevereiro não têm mais que 29 dias!")
    else:
        mes = Mes[mes]
        
    ano = data_int[2]
    if ano < 0:
        print("Ano Inválido.")
        
    print(f"{dia} de {mes} de {ano}")
     
data = input("Escreva a data no formato DD/MM/AAAA: ")
data_extenso(data)