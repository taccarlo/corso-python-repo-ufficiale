#Scrivere una funzione che prende in input una lista,
# la controlla e se contiene almeno un valore 
#che non sia un intero ritorna un errore. 
# Altrimenti la funzione ritorna una lista 
#che in prima posizione contiene il valore 
# minimo dell’input, in seconda posizione la media
# e in terza posizione contiene il valore massimo.
import numpy
def funzione(lista):

    listamod = []
    for x in range (len(lista)):
        if(type(lista[x]) != (int)):
            return "ERRORE"  
          
    listamod.append(min(lista))
    listamod.append(numpy.mean(lista))
    listamod.append(max(lista))

    return listamod
    #media = (sum(lista))/(len(lista))

lista = [3,10,5,7]
print(funzione(lista))
