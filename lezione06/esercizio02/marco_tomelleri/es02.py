'''Scrivere una funzione che data in input 
(alla funzione) una lista, ritorna una stringa 
formata dalla concatenazione degli elementi della lista.'''



def concatena(lista):
    stringa = ''
    for i in range(len(lista)):
        stringa += lista[i]
    return stringa

print(concatena(['p','i','p','p','o']))

