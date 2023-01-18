'''Scrivere e testare una funzione sostituisci
(lista,valore1,valore2)
che prende in input una lista e due valori 
e ritorna una lista in cui tutte le occorrenze
del valore1 sono sostituite da valore2
Esempio :   
print(sostituisci([‘p’,’i’,’p’,’p’,’o’],‘p’,‘l’)) 
>>> [‘l’,’i’,’l’,’l’,’o’]'''

def sostituisci(lista,valore1,valore2):
    for i in range(len(lista)):
        if lista[i]==valore1:
            lista[i]=valore2
    return lista

print(sostituisci(['p','i','p','p','o'],'p','l'))


