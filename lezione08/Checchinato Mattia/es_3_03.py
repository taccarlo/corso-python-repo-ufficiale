import random

def lancia_dado():
  return random.randint(1, 6)

def yahtzee():
  tiro = [lancia_dado(), lancia_dado(), lancia_dado(), lancia_dado(), lancia_dado()]
  print("Risultati dei tuoi dadi:", tiro)
  if len(set(tiro)) == 1:
    print("Yahtzee! Hai vinto")
  else:
    print("Mi dispiace, questa volta non hai vinto")

if __name__ == '__main__':
  yahtzee()
