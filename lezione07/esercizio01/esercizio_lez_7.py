#es1
lista01=[1,2,3,4,5,6,7,8,9,0]
val1 = 3
val2 = 11
def sostituisci(lista01,val1,val2):
    for x in lista01:
        i=lista01.index(x)
        if x == val1:
            lista01.pop(i)
            lista01.insert((i), val2)
    return lista01

print(sostituisci(lista01,val1,val2))

#es2

v1=str(input("inserire una lista di valori separati dallo spazio"))

