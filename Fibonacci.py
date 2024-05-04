"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo."""

def fibonacci(termo):
    f1_termo = 1
    f2_termo = 1
    
    f_lista = [f1_termo,f2_termo]
    for i in range(1,termo):
        fn_termo = f_lista[i] + f_lista[i-1]
        f_lista.append(fn_termo)
    
    print(f_lista)


fibonacci(100)