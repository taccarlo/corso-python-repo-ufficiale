'''
6.2) creare un programma chiamato “battaglia_risiko.py” che includerà la libreria del punto 6.1
Vengono lanciati per due volte 3 dadi (quindi 6 dadi in totale): i primi tre dadi sono quelli dell’attaccante, gli ultimi tre sono quelli del difensore. I risultati sono salvati in due liste differenti.
Ora dobbiamo ordinare in maniera decrescente le 2 liste di dadi (come nel risiko)
Infine confrontiamo i risultati dello scontro un dado alla volta (in ordine crescente)
La vittoria in uno scontro determina quante armate un giocatore ha perso. 
Stampare quindi i risultati dei dadi ordinati e quante armate ha perso ogni
giocatore
'''
import esercizio01

difesa = []
attacco = []
for x in range(3):
    difesa.append(esercizio01.lancia_dado())

for x in range(3):
    attacco.append(esercizio01.lancia_dado())

difesa = esercizio01.ordina_dadi(difesa)
attacco = esercizio01.ordina_dadi(attacco)
i = 0
for x in range(3):
    print("Difesa:  ", difesa[x])
    print("Attacco: ", attacco[x])
    counter = esercizio01.scontro(difesa[x],attacco[x])
    if(counter == True):
        i = i + 1

print("Armate vinte dalla difesa ",i,"/3")
print("Armate vinte dall'attacco ",3-i,"/3")
