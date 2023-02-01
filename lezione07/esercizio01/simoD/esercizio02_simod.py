#Scrivere una funzione che data in input 
#(alla funzione) una lista, ritorna una stringa 
#formata dalla concatenazione degli elementi della
#lista


def funzione(lista):
    stringa = ""
    for x in range (len(lista)):
        stringa = stringa + " " + str(lista[x])
        
    return stringa


lista = ["luca","mangia","le","caramelle"]

print(funzione(lista))
