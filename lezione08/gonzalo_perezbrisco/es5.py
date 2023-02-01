'''Scrivere un programma che individui il valore massimo e minimo all interno di una lista
lunga n (inserito da utente) di numeri generati casualmente da -8 a 15.'''

import random

def trova(a):
  print (max(a))
  print (min(a))
  
n = int(input("Inserisci la quantità: "))

a = []

for x in range(n):
  a.append(random.randint(-8, 15))

trova(a)