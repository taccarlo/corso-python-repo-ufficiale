'''Generare una lista lunga 20 di numeri casuali compresi 
tra n ed m inseriti da utente, a questo punto stampare
 la lista e successivamente stamparla capovolta 
 (dall ultimo elemento al primo) e raddoppiando ogni 
 numero'''

import random

n = int(input("Inserisci il valore minimo: "))
m = int(input("Inserisci il valore massimo: "))

lista = [random.randint(n, m) for i in range(20)]

print("Lista:", lista)

print("Lista capovolta e raddoppiata:", [i*2 for i in lista[::-1]])
