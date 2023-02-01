def concatena (lista):
    var = ''
    for i in range(len(lista)):
        var += lista[i]
    return var

parola = []
lunghezza = int(input('Inserisci la lunghezza della lista'))
for x in range(lunghezza):
    parola.append(input(f'Inserisci il {x} valore '))
print(parola)
print(concatena(parola))