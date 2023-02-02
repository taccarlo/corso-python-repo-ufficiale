'''
Si vuole creare un programma che riesca a gestire un distributore di merendine usando un dizionario
Usiamo al posto degli Euro i centesimi.
Il distributore contiene:
	merendine fiesta da 80 centesimi
	merendine duplo da 90 centesimi
	succhi di frutta da 45 centesimi
	oreo da 90 centesimi

Scrivere una funzione che mi indichi il più costoso, ricordando che il massimo si può trovare attraverso i comandi:
massima_chiave = max(dizionario, key=dizionario.get).

Scrivere una funzione che stampi la merendina che abbia sia il costo minore di 1 euro sia un numero di lettere pari nel nome.

Scrivere una funzione che stampi la merendina che abbia il costo minore di 50 centesimi oppure un numero di lettere pari.
'''

distributore = {"fiesta": 80 ,"duplo": 90,"frutta": 45,"oreo": 90}
massima_chiave = max(distributore, key=distributore.get)
print("Merendina che costa di più:\n", massima_chiave,"\n")

def min1_pari(distributore):
    for key in distributore:
        if((distributore[key]) < 100) and (len(key) % 2 == 0):
            print(key)

print("Merendine che costono meno di 1 euro: \n")
min1_pari(distributore)

def min50_pari(distributore):
    for key in distributore:
        if((distributore[key]) < 50) and (len(key) % 2 == 0):
            print(key)

print("\n")
print("Merendine che costono meno di 50 centesimi: \n")
min50_pari(distributore)