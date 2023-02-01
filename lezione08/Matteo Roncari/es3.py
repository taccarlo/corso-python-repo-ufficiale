import random
n = int(input("Inserire il numero di elementi "))
list = []
for i in range(n):
    list.append(random.randint(-8, 15))
min = min(list)
max = max(list)
print(list)
print(f"Il valore minimo è {min}")
print(f"Il valore massimo è {max}")