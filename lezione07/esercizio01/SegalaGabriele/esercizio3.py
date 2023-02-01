def controllo(lista):
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return ("errore")
    return [min(lista),sum(lista)/len(lista),max(lista)]

lista=(23,46,"ciao",7,7654,7654,)
print(controllo(lista))