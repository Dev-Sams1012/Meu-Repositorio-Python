time_7 = ["Naruto", "Sasuke", "Sakura", "Kakashi"] # Criação do vetor inicial com os membros do time 7
print(time_7)

time_7.remove("Sasuke") # Retirada do Sasuke, já que ele decidiu seguir um caminho diferente.
print(f"\n{time_7}")

time_7.remove("Kakashi") # Retirada do Kakashi, já que ele está de repouso por mais de 10 dias.
print(f"\n{time_7}")

time_7.append("Sai") # Adição do novo colega do time 7.
time_7.append("Yamato") # Adição do novo treinador do time 7.
print(f"\n{time_7}")

time_7.insert(time_7.index("Naruto"),"Boruto") # Troca do Naruto por seu filho, Boruto.
time_7.remove("Naruto") # Retirada do Naruto, já que ele é o novo Hokage.
print(f"\n{time_7}")