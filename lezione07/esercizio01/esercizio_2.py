"""
Scrivere una funzione che data in input 
(alla funzione) una lista, ritorna una stringa 
formata dalla concatenazione degli elementi della
 lista."""

def catenaz(lista):
    stringa=""
    stringa=stringa.join(lista[0:])
    print(stringa)

l1=["A","2"]
catenaz(l1)
