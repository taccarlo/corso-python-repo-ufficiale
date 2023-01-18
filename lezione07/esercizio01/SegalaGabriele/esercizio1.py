'''
Scrivere e testare una funzione sostituisci
(lista,valore1,valore2)
che prende in input una lista e due valori 
e ritorna una lista in cui tutte le occorrenze
del valore1 sono sostituite da valore2
Esempio :   
print(sostituisci([‘p’,’i’,’p’,’p’,’o’],‘p’,‘l’)) 
>>> [‘l’,’i’,’l’,’l’,’o’] 


Scrivere una funzione che data in input 
(alla funzione) una lista, ritorna una stringa 
formata dalla concatenazione degli elementi della
lista.


Scrivere una funzione che prende in input una lista,
 la controlla e se contiene almeno un valore 
 che non sia un intero ritorna un errore. 
 Altrimenti la funzione ritorna una lista 
 che in prima posizione contiene il valore 
 minimo dell’input, in seconda posizione la media
  e in terza posizione contiene il valore massimo.
'''

def sostituisci(lista, valore1, valore2):
    return [valore2 if i == valore1 else i for i in lista]

lista=("p","i","p","p","o")
val1="p"
val2="l"
nuova_lista= sostituisci(lista,val1,val2)
print (nuova_lista)