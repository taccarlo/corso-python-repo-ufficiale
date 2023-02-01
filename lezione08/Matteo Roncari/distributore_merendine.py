distributore = {"merendinaFiesta": 80, "merendinaDuplo": 90, "succoFrutta": 45, "oreo" : 90}

def piu_costoso ():
    return max(distributore, key=distributore.get)

def funzione1 ():
    print("Costo inferiore a 1 euro e lettere pari nel nome")
    dict_and = {}
    for i in distributore:
        if (len(i) % 2 == 0 and distributore.get(i) < 100):
            dict_and[i] = distributore[i]
    return dict_and
        

def funzione2 ():
    print("Costo inferiore a 50 centesimi o lettere pari nel nome")
    dict_or = {}
    for i in distributore:
        if (len(i) % 2 == 0 or distributore.get(i) < 50):
            dict_or[i] = distributore[i]
    return dict_or


print("La cosa più costosa è",piu_costoso())
print(funzione1())
print(funzione2())
