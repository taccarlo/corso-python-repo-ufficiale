"""Scrivere e testare una funzione sostituisci
(lista,valore1,valore2)
che prende in input una lista e due valori 
e ritorna una lista in cui tutte le occorrenze
del valore1 sono sostituite da valore2
Esempio :   
print(sostituisci([‘p’,’i’,’p’,’p’,’o’],‘p’,‘l’)) >>> [‘l’,’i’,’l’,’l’,’o’] 
"""

def sostituisci(list1,st1,st2):
    for i in range(len(list1)):
        if list1[i] == st1:
            list1[i] = st2
    print(list1)

lista = ["c","i","a","o"]
val1= "c"
val2= "z"
sostituisci(lista, val1, val2) 

