'''Scrivere e testare una funzione 
sostituisci(lista,valore1,valore2)
che prende in input una lista e due valori
e ritorna una lista in cui tutte le occorrenze 
del valore1 sono sostituite da valore2
Esempio :   
print(sostituisci([‘p’,’i’,’p’,’p’,’o’],‘p’,‘l’)) 
>>> [‘l’,’i’,’l’,’l’,’o’] 

Scrivere una funzione che data in input 
(alla funzione) una lista, ritorna una stringa 
formata dalla concatenazione degli elementi della lista.

Scrivere una funzione che prende in input una lista,
la controlla e se contiene almeno un valore che non sia 
un intero ritorna un errore. 
Altrimenti la funzione ritorna una lista che in 
prima posizione contiene il valore minimo dell’input, 
in seconda posizione la media e in terza posizione 
contiene il valore massimo.'''
#es 1

'''val_1=55
val_2=44
lista=[55,33,22,66,77,88,]
def funzione_s(lista,val_1,val_2):
    i=0
    while i<len(lista):
        if lista[i]==val_1:
            lista.pop(i)
            lista.insert(i,val_2)
        i+=1
    return lista 
print(funzione_s(lista,val_1,val_2))'''

#es 2

'''lista1=["ciao ","mi ","chiamo ","simone "]
frase=str("")
def funz_c(lista,frase):
    for x in lista1:
        frase=frase+str(x)
    return frase 
print(funz_c(lista1,frase))
print(lista1)'''

#es 3

lista_3=[11,48,23,55,44,33]



def funz_3(lista_3):
    x = 1 #variabile intera per controllare la classe degli elemnti della lista
    copia=[]
    min=[]
    magg=[]
    i=0
    somma=0
    while i<len(lista_3):
        if type(lista_3[i]) != type(x):
            print("Error")
        else:
            somma+=lista_3[i]
        i+=1
    media=somma/i
    
    minimo=1000000000000
    for x in range (len(lista_3)):
        if lista_3[x]<minimo:
            minimo=lista_3[x]
    media=sum(lista_3)/len(lista_3)
    massimo=0
    for x in range (len(lista_3)):
        if lista_3[x]>massimo:
            massimo=lista_3[x]
    newlist=[minimo,media,massimo,]
    return newlist

print(funz_3(lista_3))    
            
