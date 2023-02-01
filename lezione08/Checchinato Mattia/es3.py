import random

n = int(input("Inserire la lunghezza della lista (n): "))

random_numbers = []

for i in range(n):
    random_numbers.append(random.randint(-8, 15))

print("Lista di numeri casuali: ", random_numbers)

max_value = max(random_numbers)
min_value = min(random_numbers)

print("Il valore massimo è: ", max_value)
print("Il valore minimo è: ", min_value)

