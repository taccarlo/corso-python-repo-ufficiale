def concatenazione(lista):
    stringa = ""
    for x in range(len(lista)):
        stringa = stringa + " " + str(lista[x])
    return stringa

lista = ("ciao", "mi", "chiamo", "tommaso")

print(concatenazione(lista))