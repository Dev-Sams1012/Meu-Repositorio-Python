valor = float(input("Valor original da compra: "))
desconto = (int(input("Porcentagem de desconto: ")))/100
imposto = (int(input("Taxa de imposto (porcentagem): ")))/100

valor_descontado = valor - (valor*desconto)
valor_final = valor_descontado + (imposto * valor_descontado)

print(valor_final)