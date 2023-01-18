'''
Data una lista di numeri restituire una lista in cui tutti 
gli elementi adiacenti uguali sono stati ridotti 
ad un singolo elemento.
Esempio:
con [1,2,2,3,2,2,3] la funzione ritorna [1,2,3,2,3]
Nota: si può sia restituire una nuova lista sia modificare quella passata come argomento.
'''

def funzione(lista):
    
    listamod = []
    for x in range (len(lista)):
        if x not in listamod:
            listamod.append(lista[x])
    
    return listamod

lista = [1,2,2,3,2,2,3]
print(funzione(lista))

