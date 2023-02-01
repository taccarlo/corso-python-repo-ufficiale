import random

n = int(input("Inserire il valore di n: "))
m = int(input("Inserire il valore di m: "))

random_numbers = []

for i in range(20):
    random_numbers.append(random.randint(n, m))

print("Lista originale: ", random_numbers)

reversed_doubled_list = [2 * i for i in random_numbers[::-1]]

print("Lista capovolta e raddoppiata: ", reversed_doubled_list)