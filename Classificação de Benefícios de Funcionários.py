anos = int(input("Tempo de serviço (anos): "))

if anos > 0:
    if anos < 1:
        beneficio = "Benefício Básico"
    elif anos >= 1 and anos < 3:
        beneficio = "Benefício Intermediário"
    elif anos >= 3 and anos < 5:
        beneficio = "Benefício Avançado"
    elif anos >= 5:
        beneficio = "Benefício Premium"
else:
    beneficio = "inválido"
    
print(beneficio)