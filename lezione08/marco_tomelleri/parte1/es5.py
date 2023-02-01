'''Scrivere un programma che individui il valore massimo e minimo all’interno di una lista
lunga n (inserito da utente) di numeri generati casualmente da -8 a 15'''

import random

def main():

    n = int(input("Inserisci il numero di elementi della lista: "))
    lista = []
    for i in range(n):
        lista.append(random.randint(-8, 15))
    print(lista)
    print("Il valore massimo è: ", max(lista))
    print("Il valore minimo è: ", min(lista))

if __name__ == "__main__":
    main()