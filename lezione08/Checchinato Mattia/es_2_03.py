import random

def lancia_dado():
  return random.randint(1, 6)

def scontro(difensore, attaccante):
  if difensore >= attaccante:
    return True
  else:
    return False

def ordina_dadi(lista):
  return sorted(lista, reverse=True)

def battaglia_risiko():
  attaccante = [lancia_dado(), lancia_dado(), lancia_dado()]
  difensore = [lancia_dado(), lancia_dado(), lancia_dado()]
  
  attaccante_ordinato = ordina_dadi(attaccante)
  difensore_ordinato = ordina_dadi(difensore)
  
  perdita_attaccante = 0
  perdita_difensore = 0
  
  for i in range(min(len(attaccante), len(difensore))):
    if scontro(difensore_ordinato[i], attaccante_ordinato[i]):
      perdita_attaccante += 1
    else:
      perdita_difensore += 1
  
  print("Risultati dei dadi dell'attaccante:", attaccante_ordinato)
  print("Risultati dei dadi del difensore:", difensore_ordinato)
  print("Il numero di armate perse dall'attaccante è:", perdita_attaccante)
  print("Il numero di armate perse dal difensore è:", perdita_difensore)

if __name__ == '__main__':
  battaglia_risiko()