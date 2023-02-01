import random

def genera(min, max):
  a = []
  for x in range(20):
    a.append(random.randint(int(min), int(max)))
  return a

def stampa_contrario(a):
  for x in range(20):
    a[x] = a[x]*2
  a.reverse()
  return a
  
min = input("Inserisci min: ")
max = input("Inserisci max: ")

a = genera(min, max)

print(a)

print(stampa_contrario(a))

