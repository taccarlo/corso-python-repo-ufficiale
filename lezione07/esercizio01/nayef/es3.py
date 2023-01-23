def controlla (lista):
    a=False
    for i in range (len(lista)):
        if (lista[i]*10)%10!=0:
            a=True
    if a==True:
        return "errore"
    else:
        risultato=[min(lista), sum(lista)/len(lista), max(lista)]

        return risultato


lista1=[]
lungo= int (input ("inserire lunghezza"))
for x in range(lungo):
    lista1.append(float(input ("inserisci elemento :")))

print(controlla(lista1))
        