def controllo(lista):
    for elemento in lista:
        if not isinstance(elemento, int):
            return "Errore: la lista contiene un valore che non è un intero"
    min_val = min(lista)
    max_val = max(lista)
    avg_val = sum(lista) / len(lista)
    return (min_val, max_val, avg_val)

#test

lista = [2,3,5,6,78,9,9.8]
print(controllo(lista))