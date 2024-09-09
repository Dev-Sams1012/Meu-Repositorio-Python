valor_total = int(input("Valor total da compra: "))
valor_pago = int(input("Valor pago pelo cliente: "))
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
troco = valor_pago - valor_total
troco_print = troco

if troco > 0:
    if troco >= 100:
        nota_100 = troco // 100
        troco -= 100*nota_100
    if troco >= 50:
        nota_50 = troco // 50
        troco -= 50*nota_50
    if troco >= 20:
        nota_20 = troco // 20
        troco -= 20*nota_20
    if troco >= 10:
        nota_10 = troco // 10
        troco -= 10*nota_10
    if troco >= 5:
        nota_5 = troco // 5
        troco -= 5*nota_5
    if troco >= 2:
        nota_2 = troco // 2
        troco -= 2*nota_2

print(f"Troco: {troco_print}\nCédulas:\nR$100: {nota_100}\nR$50: {nota_50}\nR$20: {nota_20}\nR$10: {nota_10}\nR$5: {nota_5}\nR$2: {nota_2}")