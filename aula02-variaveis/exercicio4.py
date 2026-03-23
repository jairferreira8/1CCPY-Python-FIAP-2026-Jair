print("""Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro
levou para percorrer essa distância?""")

input("Pressione enter para exibir contas e resultado: ")

print("Distancia = 150km")
print("Velocidade media = 60km/h")

print("Tempo levado = distancia / velocidade")

velocidade = 60
distancia = 150
tempo  = distancia / velocidade
horas = (int(tempo))
minutos = int (int(horas - tempo) * 60)

print("A viagem levou {horas}:{minutos} para ser concluída.")

