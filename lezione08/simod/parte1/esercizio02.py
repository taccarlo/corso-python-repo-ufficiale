import random

n = int(input("Inserire un numero da cui partire: "))
m = int(input("Inserire un numero da cui partire: "))

lista = []

for x in range(1,21):
    lista.append(random.randrange(n,m))

print(lista)

print("LISTA RADDOPPIATA E GIRATA:\n")


for x in range(20):
    lista[x] = lista[x] * 2

lista.reverse()

print(lista)
 