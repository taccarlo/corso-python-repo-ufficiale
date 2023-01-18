def unisci(lista1,lista2):
    lista3=lista1+lista2
    lista3.sort()
    return lista3

lista1=[]
lista2=[]

lungo1= int (input ("inserire lunghezza"))
for x in range(lungo1):
    lista1.append(int (input ("inserisci elemento :")))

lungo2= int (input ("inserire lunghezza"))
for x in range(lungo2):
    lista2.append(int (input ("inserisci elemento :")))

print (unisci(lista1,lista2))