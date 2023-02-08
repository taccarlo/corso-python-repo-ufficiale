import random

num = []
n = int(input())
m = int(input())

for i in range(20):
  num.append(random.randint(n, m))

print(num)

num.reverse()
for i in range(20):
  num[i] *= 2

print(num)