n1 = float(input("Escolha o primeiro valor "))
n2 = float(input("Escolha o segundo valor "))
operacao = input("Escolha a operação dentre as seguintes: \
+ para soma, - para subtração, * para multiplicação \
e / para divisão. ")

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

if operacao == "+":
    print(n1, "+", n2, "=", soma)
elif operacao == "-":
    print(n1, "-", n2, "=", sub)
elif operacao == "*":
    print(n1, "*", n2, "=", mult)
elif operacao == "/":
    if n2 == 0:
        print("Essa divisão não é possível")
    else:
        print (n1, "/", n2, "=", div)