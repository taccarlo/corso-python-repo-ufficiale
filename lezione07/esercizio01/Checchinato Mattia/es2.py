def concatenazione(lista):
    stringa = ""
    for elemento in lista:
        stringa += str(elemento)
    return stringa

#test

lista = [2,4,5,1,3,7,6,9]

print(concatenazione(lista))