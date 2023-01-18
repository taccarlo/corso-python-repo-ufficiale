'''
Date due liste ordinate in ordine crescente, creare e restituire un’unica lista di tutti gli elementi ordinati.
E’ possibile modificare le liste passate come argomenti.
Idealmente l’algoritmo dovrebbe implicare una singola iterazione su ciascuna lista.
Suggerimento: le liste sono ordinate: confrontare il primo elemento delle due liste ed aggiungere il più piccolo alla lista da restituire come risultato (rimuovendolo dalla lista originaria). Continuare fino a che una delle due liste non si svuota.
'''

def ordina(a, a2):
  a.extend(a2)
  a.sort()
  return a

print(ordina([1, 2, 3, 4], [2, 1, 5, 6]))