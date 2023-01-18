lista1=[]
lungo= int (input ("inserire lunghezza"))
for x in range(lungo):
    lista1.append(input ("inserisci elemento :"))
print (lista1)

i=0
j=len(lista1)

while i<j:
    if i>=1 and lista1[i]==lista1[i-1]:
        lista1.pop(i)
        j=len(lista1)
    i=i+1
print (lista1)
