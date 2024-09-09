tempo = int(input("Tempo de exercícios cardiovasculares (minutos): "))
serie = int(input("Número de séries de exercícios de força: "))
agua = int(input("Quantidade de água consumida (ml): "))
aquecimento = input("O membro fez aquecimento? (Sim/Não): ")

if tempo >= 30 and serie >= 3 and agua >= 500 and aquecimento == "Sim":
    print("O membro está em bom estado de saúde.")
else:
    print("O membro não está em bom estado de saúde.")