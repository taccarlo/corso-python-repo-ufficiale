'''
Data una lista di numeri restituire una lista in cui tutti gli elementi adiacenti uguali sono stati ridotti ad un singolo elemento.
Esempio:
con [1,2,2,3,2,2,3] la funzione ritorna [1,2,3,2,3]
Nota: si può sia restituire una nuova lista sia modificare quella passata come argomento.
'''

def cancella(a):
  m=-1
  for i in range(len(a)-1):
    m+=1
    if a[m] == a[m+1]:
      del a[m+1]
      m-=1
  return a

print(cancella([1,2,2,3,2,2,3]))