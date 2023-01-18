def controllo (lista):
    float = False
    for i in range (len(lista)):
        if (lista[i]*10)%10!=0:
            float = True
    if float:
        return "Errore!"
    else:
        res = [min(lista), sum(lista)/len(lista), max(lista)]
        return res

lis = []
lunghezza = int(input('Inserisci la lunghezza della lista '))
for x in range(lunghezza):
    lis.append(float(input(f'Inserisci il {x} valore ')))
print(controllo(lis))