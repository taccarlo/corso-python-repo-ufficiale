import random

n = int(input())
num = []

for i in range(n):
  num.append(random.randint(-8, 15))

print(max(num), min(num))