import random

n = int(input("quanto lunga la vuoi la lista? : "))
lista = []
for i in range(n):
    lista.append(random.randint(-8, 15))
print(lista)
print("Il valore massimo è: ", max(lista))
print("Il valore minimo è: ", min(lista))

