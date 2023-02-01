'''
Si vuole creare un programma che riesca a gestire un distributore di merendine usando un dizionario
Usiamo al posto degli Euro i centesimi.
Il distributore contiene:
	merendine fiesta da 80 centesimi
	merendine duplo da 90 centesimi
	succhi di frutta da 45 centesimi
	oreo da 90 centesimi
'''
merendine = {"fiesta":80,"duplo":90,"succo di frutta":45,"oreo":90}
'''
Scrivere una funzione che mi indichi il più costoso, ricordando che il massimo si può trovare attraverso i comandi:
massima_chiave = max(dizionario, key=dizionario.get).
'''
def massimo():
    list = []
    massima_chiave = max(merendine, key = merendine.get)
    for x in merendine:
        if merendine[x] == merendine[massima_chiave]:
            list.append(x)
    return list

'''
Scrivere una funzione che stampi la merendina che abbia sia il costo minore di 1 euro sia un numero di lettere pari nel nome.
'''
def pari_euro():
    list = []
    for x in merendine:
        if merendine[x] < 100 and len(x)%2==0:
            list.append(x)
    return list


'''
Scrivere una funzione che stampi la merendina che abbia il costo minore di 50 centesimi oppure un numero di lettere pari.
'''

def fifty_cent():
    list = []
    for x in merendine:
        if merendine[x] < 50 or len(x)%2==0:
            list.append(x)
    return list