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
    listamod.append(lista[0])
    for x in range (1,len(lista)):
        if (lista[x] != lista[x-1]):
            listamod.append(lista[x])
            
    
    return listamod

lista = [1,2,2,3,2,2,3]
print(funzione(lista))

