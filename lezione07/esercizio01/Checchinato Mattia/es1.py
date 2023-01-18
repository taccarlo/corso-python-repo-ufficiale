def sostituisci(lista, valore1,valore2):
    for i in range(len(lista)):
        if lista[i] == valore1:
            lista[i] == valore2
        return lista
    
#test

lista = [1,3,4,5,6,2,7,8,9]

valore1 = 4
valore2 = 7

print(sostituisci(lista, valore1, valore2))