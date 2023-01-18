'''
Date due liste ordinate in ordine crescente, creare e restituire un’unica lista di tutti gli elementi ordinati.
E’ possibile modificare le liste passate come argomenti.
Idealmente l’algoritmo dovrebbe implicare una singola iterazione su ciascuna lista.
Suggerimento: le liste sono ordinate: confrontare il primo elemento delle due liste ed aggiungere il più piccolo alla lista da restituire come risultato (rimuovendolo dalla lista originaria). Continuare fino a che una delle due liste non si svuota.
'''

def merge(list1, list2):
    result = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1)
    result.extend(list2)
    return result

if __name__ == '__main__':
    print(merge([1, 2, 3, 4], [2, 3, 4, 5]))
    print(merge([1, 2, 3, 4], [2, 3, 4, 5, 6]))
    print(merge([1, 2, 3, 4, 5], [2, 3, 4, 5]))
    print(merge([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
    print(merge([1, 2, 3, 4, 5, 6], [2, 3, 4, 5]))
    print(merge([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6]))

    