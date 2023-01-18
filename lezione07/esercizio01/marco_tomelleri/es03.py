'''Scrivere una funzione che prende in input una lista,
 la controlla e se contiene almeno un valore 
 che non sia un intero ritorna un errore. 
 Altrimenti la funzione ritorna una lista 
 che in prima posizione contiene il valore 
 minimo dell’input, in seconda posizione la media
  e in terza posizione contiene il valore massimo.'''

def lista(lista):
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return "Errore"
    else:
        return [min(lista), sum(lista)/len(lista), max(lista)]

print(lista([1,2,3,4.5,5,6,7,8,9,10]))


