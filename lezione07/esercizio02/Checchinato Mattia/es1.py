def riduci_elementi_uguali(lista):
    nuova_lista = []
    ultimo_elemento = None
    for elemento in lista:
        if elemento != ultimo_elemento:
            nuova_lista.append(elemento)
            ultimo_elemento = elemento
    return nuova_lista

#test

lista = [1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]

print(riduci_elementi_uguali(lista))
        