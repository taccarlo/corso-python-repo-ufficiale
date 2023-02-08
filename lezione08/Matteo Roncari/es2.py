import random
min = int(input("Inserire il valore minimo "))
max = int(input("Inserire il valore massimo "))
lista = []
for i in range(20):
    lista.append(random.randint(min, max))
print(lista)
lista.reverse()
for i in range(len(lista)):
    lista[i] *= 2

print(lista)