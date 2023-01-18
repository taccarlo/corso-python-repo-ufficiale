def stringa(lista):
    a=""
    for i in range(len(lista)):
        a += lista[i]
    return a

lista1=[]
lungo= int (input ("inserire lunghezza"))
for x in range(lungo):
    lista1.append(input ("inserisci elemento :"))

print (stringa(lista1))
