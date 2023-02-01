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
list02=list(v1.split())
print (list02)

def string(x):
    delimitat=" "
    frase = delimitat.join(x)
    return frase

print (string(list02))

#es3

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