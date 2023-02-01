'''Facendo riferimento all’esercizio 6 potete trovare molti giochi basati sul semplice lancio di dadi come ad esempio Yahtzee o Poker (coi dadi). Provate, se avete tempo e voglia, a realizzare una versione (anche minimale) di questi giochi'''




import random
import es6_1

def yahtzee():
    lista_dadi = []
    for i in range(0, 5):
        lista_dadi.append(es6_1.lancia_dado())
    print("Lista dadi: ", lista_dadi)
    if lista_dadi[0] == lista_dadi[1] == lista_dadi[2] == lista_dadi[3] == lista_dadi[4]:
        print("Hai fatto Yahtzee!")
    else:
        print("Non hai fatto Yahtzee!")

def main():
    yahtzee()

if __name__ == '__main__':
    main()
