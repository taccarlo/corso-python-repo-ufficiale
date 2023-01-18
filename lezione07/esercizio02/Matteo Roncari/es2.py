def unisci (lista1, lista2):
    lista3 = lista1 + lista2
    lista3.sort()
    return lista3

def inserisci_lista():
    lis = []
    lunghezza = int(input('Inserisci la lunghezza della lista '))
    for x in range(lunghezza):
            lis.append(float(input(f'Inserisci il {x} valore ')))
    lis.sort()
    return lis

lis1 = inserisci_lista()
lis2 = inserisci_lista()
lis3 = unisci(lis1, lis2)
print(lis3)