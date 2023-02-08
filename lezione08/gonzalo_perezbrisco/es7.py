import random

def lancia_dado():
  return random.randint(1, 6)

def scontro( difensore, attaccante):
  if difensore >= attaccante:
    return True
  else:
    return False

def ordina_dadi(lista):
  lista.sort()
  lista.reverse()
  return lista