'''
Data una lista di numeri restituire una lista in cui tutti gli elementi adiacenti uguali sono stati ridotti ad un singolo elemento.
Esempio:
con [1,2,2,3,2,2,3] la funzione ritorna [1,2,3,2,3]
Nota: si può sia restituire una nuova lista sia modificare quella passata come argomento.
'''

def remove_adjacent(nums):
    result = []
    for num in nums:
        if len(result) == 0 or result[-1] != num:
            result.append(num)
    return result

if __name__ == '__main__':

    print(remove_adjacent([1, 2, 2, 3]))
    print(remove_adjacent([2, 2, 3, 3, 3]))
    print(remove_adjacent([]))

    