import random

def lancia_dado():
  n = random.randint(1, 6)
  return n

def scontro(dif, att):
  return True if dif >= att else False

def ordina_dadi(list):
  list.sort(reverse=True)
  return list