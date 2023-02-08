merendine = {'Fiesta':80, 'Duplo':90, 'Succo di frutta': 45, 'oreo': 85}

def piu_costoso(merendine):
    return max(merendine, key=merendine.get)


def minore_uno_e_pari(a):
    dizionario = {}
    for x in a:
        if len(x)%2==0 and a[x]<100:
            dizionario[x]=a[x]
    return dizionario 

def minore_o_pari(a):
    dizionario = {}
    for x in a:
        if len(x)%2==0 or a[x]<50:
            dizionario[x]=a[x]
    return dizionario 

print ('la merendina più costosa è: ', piu_costoso(merendine))
print("La merendina con costo minore di 1 euro e pari nel nome è:", minore_uno_e_pari(merendine))
print("La merendina con il costo minore di 50 cent. oppure con il nome pari è:", minore_o_pari(merendine))
