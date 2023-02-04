'''creare un programma chiamato “battaglia_risiko.py” che includerà la libreria del punto 6.1
Vengono lanciati per due volte 3 dadi (quindi 6 dadi in totale): i primi tre dadi sono quelli dell’attaccante, gli ultimi tre sono quelli del difensore. I risultati sono salvati in due liste differenti.
Ora dobbiamo ordinare in maniera decrescente le 2 liste di dadi (come nel risiko)
Infine confrontiamo i risultati dello scontro un dado alla volta (in ordine crescente)
La vittoria in uno scontro determina quante armate un giocatore ha perso. 
Stampare quindi i risultati dei dadi ordinati e quante armate ha perso ogni giocatore'''


import dadi

attack = []
dif = []

def difensore():
    for i in range(3):
        dif.append(dadi.lancia_dado())
    return dif

def attacante():
    for x in range(3):
        attack.append(dadi.lancia_dado())
    return attack

print('Numeri attaccante: ', dadi.ordina_dadi(difensore()))
print('Numeri difensori: ', dadi.ordina_dadi(attacante()))

punti_attacante = 0
punti_difensore = 0
for x in range(2, -1, -1):
  if(dadi.scontro(dif[x], attack[x]) == True):
    punti_difensore+=1
  else:
    punti_attacante+=1

print("\nL'attacante ha perso: ", punti_attacante, " truppe")
print("L'difensore ha perso: ", punti_difensore, " truppe\n")

            



        



    




