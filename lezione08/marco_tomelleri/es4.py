'''Generare una lista lunga 20 di numeri casuali compresi tra n ed m inseriti da utente, a
questo punto stampare la lista e successivamente stamparla capovolta (dall’ultimo
elemento al primo) e raddoppiando ogni numero'''

import random

def main():
    n = int(input("Inserisci il primo numero: "))
    m = int(input("Inserisci il secondo numero: "))
    lista = []
    for i in range(20):
        lista.append(random.randint(n, m))
    print(lista)
    lista.reverse()
    print(lista)
    for i in range(len(lista)):
        lista[i] *= 2
    print(lista)

if __name__ == "__main__":
    main()
    