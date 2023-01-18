def sostituisci(lista, val1, val2):
    for i in range (len(lista)):
        if(lista[i] == val1):
            lista[i] = val2
    return lista

lista = ['q', 'r', 'q', 'q', 'r']
val1 = input("Inserisci un valore da sostituire: ")
val2 = input("Inserisci un valore che sostituisce: ")

print(sostituisci(lista, val1, val2))