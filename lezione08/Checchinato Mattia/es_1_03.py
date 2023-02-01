import random

def lancia_dado():
  return random.randint(1, 6)

def scontro(difensore, attaccante):
  if difensore >= attaccante:
    print("True") 
  else:
    print("False")

def ordina_dadi(lista):
  return sorted(lista, reverse=True)
