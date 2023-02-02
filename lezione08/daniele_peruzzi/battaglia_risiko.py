'''
6.2) creare un programma chiamato “battaglia_risiko.py” che includerà la libreria del punto 6.1
Vengono lanciati per due volte 3 dadi (quindi 6 dadi in totale): i primi tre dadi sono quelli dell’attaccante, gli ultimi tre sono quelli del difensore. I risultati sono salvati in due liste differenti.
Ora dobbiamo ordinare in maniera decrescente le 2 liste di dadi (come nel risiko)
Infine confrontiamo i risultati dello scontro un dado alla volta (in ordine crescente)
La vittoria in uno scontro determina quante armate un giocatore ha perso. 
Stampare quindi i risultati dei dadi ordinati e quante armate ha perso ogni
giocatore
'''

'''
7) Facendo riferimento all’esercizio 6 potete trovare molti giochi basati sul semplice lancio di dadi come ad esempio Yahtzee o Poker (coi dadi). Provate, se avete tempo e voglia, a realizzare una versione (anche minimale) di questi giochi.
'''
import dadi_lib

attack_list = []
defend_list = []

def attaccante():
    for x in range(3):
        attack_list.append(dadi_lib.lancia_dado())
    return attack_list

def difensore():
    for x in range(3):
        defend_list.append(dadi_lib.lancia_dado())
    return defend_list

dadi_lib.ordina_dadi(attaccante())
dadi_lib.ordina_dadi(difensore())

def risultati(a,b):
    def_win=0
    for x in range(-1,-len(a)-1,-1):
        if dadi_lib.scontro(b[x],a[x]):
            def_win+=1
    return print("Il risultato è ",def_win," a ",len(a)-def_win," per il difensore")

risultati(attack_list,defend_list)