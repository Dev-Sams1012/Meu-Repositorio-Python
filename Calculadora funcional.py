def soma():
    result = number_1 + number_2
    print(f"{number_1} + {number_2} = {result}")

def subtracao():
    result = number_1 - number_2
    print(f"{number_1} - {number_2} = {result}")

def multiplicação():
    result = number_1 * number_2
    print(f"{number_1} * {number_2} = {result}")

def divisao():
    if number_2 !=0:
        result = number_1 / number_2
        result = round(result,2)
        print(f"{number_1} / {number_2} = {result}")
    else:
        print("Essa divisão não pode ser feita.")

def potência():
    result = number_1 ** number_2
    print(f"{number_1} elevado à {number_2} = {result}")

def raiz():
    result = number_2 ** (1/number_1)
    result = round(result,2)
    print(f"raiz índice {number_1} de {number_2} = {result}")

counter = "s"
while counter == "s":
    print("\n 0 = Soma\n 1 = Subtração\n 2 = Multiplicação\n 3 = Divisão\n 4 = Potência\n 5 = Raiz")
    operation = int(input("Escolha a operação { 0, 1, 2, 3, 4 ou 5}: "))
    if operation <0 or operation >5:
        print("Essa operação não existe.")
    else:
        if operation == 3:
            print("O primeiro valor é o Dividendo.\nO segundo valor é o Divisor.\n")
        if operation == 5:
            print("O primeiro valor é o índice.\nO segundo valor é o Radicando.\n")
        number_1 = float(input("Primeiro valor: "))
        number_2 = float(input("Segundo valor: "))

    if operation == 0:
        soma()
    elif operation == 1:
        subtracao()
    elif operation  == 2:
        multiplicação()
    elif operation == 3:
        divisao()
    elif operation == 4:
        potência()
    elif operation == 5:
        raiz()
    counter = input("Deseja continuar? {s ou n} ")