'''6.1)   Creare una libreria con 3 funzioni:
lancia_dado(): simula il lancio di un dado a 6 facce e ne ritorna il risultato
scontro( difensore, attaccante): ritorna True in caso il difensore sia un numero più alto, viceversa False. In caso di pareggio vince il difensore.
ordina_dadi(lista): ordina in modo decrescente una lista di interi
'''

import random


def lancia_dado():
    return random.randint(1, 6)

    
