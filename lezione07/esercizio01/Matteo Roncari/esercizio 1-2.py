def sostituisci (lista, val1, val2):
    for i in range(len(lista)):
        if lista[i] == val1:
            lista[i] = val2
    return lista

parola = []
lunghezza = int (input('Inserisci la lunghezza della lista '))
for x in range(lunghezza):
    parola.append(input (f'Inserisci il {x} valore '))

trova = input('Inserisci il valore da trovare ')
n = input('Inserisci il valore con cui sostituirlo ')
print(parola)
print(sostituisci (parola, trova, n))