"""Scrivere una funzione che prende in input una lista,
 la controlla e se contiene almeno un valore 
 che non sia un intero ritorna un errore. 
 Altrimenti la funzione ritorna una lista 
 che in prima posizione contiene il valore 
 minimo dell’input, in seconda posizione la media
  e in terza posizione contiene il valore massimo.
"""

def controllo(lista) :
    for i in lista:
        if i != int(valore):
            print("Errore")
            else:
                minimo = min.(lista)
                media = sum(lista)/len(lista)
                massimo = max(lista)
                lista.insert(0, minimo)
                lista.insert(1, media)
                lista.insert(2, massimo)
    print(lista)
l1=[10, 15, 3,5]
controllo(l1)