import es7

punti_attacante = 0
punti_difensore = 0
attacante = []
difensore = []

for x in range(6):
  if (x > 2):
    difensore.append(es7.lancia_dado())
  else:
    attacante.append(es7.lancia_dado())

es7.ordina_dadi(attacante)
es7.ordina_dadi(difensore)

print ("\nNumeri dell'attaccante: ", attacante)
print ("Numeri del difensore: ", difensore)

for x in range(2, -1, -1):
  if(es7.scontro(difensore[x], attacante[x]) == True):
    punti_attacante+=1
  else:
    punti_difensore+=1

print("\nL'attacante ha perso: ", punti_attacante, " truppe")
print("L'difensore ha perso: ", punti_difensore, " truppe\n")