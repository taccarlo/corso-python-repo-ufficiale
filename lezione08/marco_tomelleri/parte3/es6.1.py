'''6.1)   Creare una libreria con 3 funzioni:
lancia_dado(): simula il lancio di un dado a 6 facce e ne ritorna il risultato
scontro( difensore, attaccante): ritorna True in caso il difensore sia un numero più alto, viceversa False. In caso di pareggio vince il difensore.
ordina_dadi(lista): ordina in modo decrescente una lista di interi
'''

import random


def lancia_dado():
    return random.randint(1, 6)


def scontro(difensore, attaccante):
    if difensore > attaccante:
        return True
    else:
        return False


def ordina_dadi(lista):
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp

    return lista


def main():
    print(lancia_dado())
    print(scontro(5, 6))
    print(ordina_dadi([1, 2, 3, 4, 5, 6]))

if __name__ == '__main__':
    main()
    