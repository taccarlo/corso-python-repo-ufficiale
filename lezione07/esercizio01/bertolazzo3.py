def funzione(lista):
    listamod = []
    for x in range (len(lista)):
        if (type(lista[x]) != (int)):
           return "errore"
    listamod.append(min(lista))
    listamod.append((sum(lista))/(len(lista)))
    listamod.append(max(lista))
    return listamod

lista = [1, 2, 3, 4, 5, 6, 7]

print(funzione(lista))