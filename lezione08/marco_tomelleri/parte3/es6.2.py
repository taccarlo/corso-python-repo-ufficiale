'''6.2) creare un programma chiamato “battaglia_risiko.py” che includerà la libreria del punto 6.1
Vengono lanciati per due volte 3 dadi (quindi 6 dadi in totale): i primi tre dadi sono quelli dell’attaccante, gli ultimi tre sono quelli del difensore. I risultati sono salvati in due liste differenti.
Ora dobbiamo ordinare in maniera decrescente le 2 liste di dadi (come nel risiko)
Infine confrontiamo i risultati dello scontro un dado alla volta (in ordine crescente)
La vittoria in uno scontro determina quante armate un giocatore ha perso. 
Stampare quindi i risultati dei dadi ordinati e quante armate ha perso ogni
giocatore'''

import random
import es6_1

def battaglia_risiko():
    lista_attaccante = []
    lista_difensore = []
    for i in range(0, 3):
        lista_attaccante.append(es6_1.lancia_dado())
        lista_difensore.append(es6_1.lancia_dado())
    lista_attaccante = es6_1.ordina_dadi(lista_attaccante)
    lista_difensore = es6_1.ordina_dadi(lista_difensore)
    armate_perso_attaccante = 0
    armate_perso_difensore = 0
    for i in range(0, 3):
        if es6_1.scontro(lista_difensore[i], lista_attaccante[i]):
            armate_perso_attaccante += 1
        else:
            armate_perso_difensore += 1
    print("Lista attaccante: ", lista_attaccante)
    print("Lista difensore: ", lista_difensore)
    print("Armate perse dall'attaccante: ", armate_perso_attaccante)
    print("Armate perse dal difensore: ", armate_perso_difensore)

def main():
    battaglia_risiko()

if __name__ == '__main__':
    main()