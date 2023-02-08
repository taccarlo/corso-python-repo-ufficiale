
'''Scrivere un programma che individui il valore 
massimo e minimo all’interno di una lista lunga
 n (inserito da utente) di numeri generati casualmente 
 da -8 a 15.
'''
import random
lung = int(input("inserire lunghezza lista:"))
lista = []
for x in range(lung):
    lista.append(random.randrange(-8,15))

print(lista)
print(min(lista))
print(max(lista))
