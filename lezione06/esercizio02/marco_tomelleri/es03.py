'''Scrivere una funzione che prende in input una lista,
la controlla e se contiene almeno un valore che non sia 
un intero ritorna un errore. 
Altrimenti la funzione ritorna una lista che in 
prima posizione contiene il valore minimo dell’input, 
in seconda posizione la media e in terza posizione 
contiene il valore massimo.
'''

def min_med_max(lista):
    if not all(isinstance(x, int) for x in lista):
        raise TypeError("La lista deve contenere solo interi")
    else:
        return [min(lista), sum(lista)/len(lista), max(lista)]

print(min_med_max([1,2,3,4,5,6,7,8,9,10]))
print(min_med_max([1,2,3,4,5,6,7,8,9,10.5]))
print(min_med_max([1,2,3,4,5,6,7,8,9,'10']))
