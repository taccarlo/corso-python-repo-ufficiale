'''Scrivere un programma che individui il valore 
massimo e minimo all interno di una lista lunga
 n (inserito da utente) di numeri generati casualmente 
 da -8 a 15.'''

import random

n = int(input("Inserisci la lunghezza della lista: "))

lista = [random.randint(-8, 15) for i in range(n)]
max_val = max(lista)
min_val = min(lista)

print("Valore massimo:", max_val)
print("Valore minimo:", min_val)



 