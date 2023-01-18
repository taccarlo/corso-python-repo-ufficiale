def sostituisci(lista,valore1,valore2):
    for x in range (len(lista)):
        if(lista[x] == valore1):
            lista[x] = valore2
    return lista

lista1 = ["p","i","p","p","o"] 

valore1 = input("inserire valore 1 da sostituire: ")
valore2 = input("inserire valore 2 che sostituisce il valore 1: ")
print(sostituisci(lista1,valore1,valore2))

