def sostituisci (lista,valore1,valore2):
    for i in range (len(lista)):
        if lista[i]==(valore1):
            lista[i]=(valore2)
    return lista

lista1= []
lungo= int (input ("inserire lunghezza"))
for x in range(lungo):
    lista1.append(input ("inserisci elemento :"))

val1= input("inserire")

val2= input("inserire")

print (sostituisci(lista1,val1,val2))