'''
Date due liste ordinate in ordine crescente, 
creare e restituire un’unica lista di tutti gli 
elementi ordinati.
E’ possibile modificare le liste passate come 
argomenti.
Idealmente l’algoritmo dovrebbe implicare una 
singola iterazione su ciascuna lista.
Suggerimento: le liste sono ordinate: 
confrontare il primo elemento delle due liste 
ed aggiungere il più piccolo alla lista da 
restituire come risultato 
(rimuovendolo dalla lista originaria). 
Continuare fino a che una delle due liste non 
si svuota.
'''

lista1 = [1,3,5,7]
lista2 = [2,4,6,8]

lista_tot = sorted((lista1+lista2))
print(lista_tot)
