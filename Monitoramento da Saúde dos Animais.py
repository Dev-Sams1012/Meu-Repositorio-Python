estrela = 0
p1 = input("O animal está ativo?")
if p1 == "sim":
    estrela += 1
    p2 = input("O animal está comendo bem?")
    if p2 == "sim":
        estrela += 1
    p3 = input("O animal está bebendo água regularmente?")
    if p3 == "sim":
        estrela += 1
    p4 = input(" O animal tem pelagem brilhante (ou pele saudável)?")
    if p4 == "sim":
        estrela += 1
    p5 = input(" O animal está dentro do peso ideal?")
    if p5 == "sim":
        estrela += 1
   
if estrela > 3:
    print(f"O animal passou no teste com {estrela} estrelas.")
elif estrela <= 3 or p1 != "sim":
    print(f"O animal não passou no teste.")