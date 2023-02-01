'''Si vuole creare un programma che riesca a gestire un distributore di merendine usando un dizionario
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


def merendina_piu_costosa(dizionario):
    massima_chiave = max(dizionario, key=dizionario.get)
    print("La merendina più costosa è: " + massima_chiave + " e costa " + str(dizionario[massima_chiave]) + " centesimi")


def merendina_meno_costosa(dizionario):
    minima_chiave = min(dizionario, key=dizionario.get)
    print("La merendina meno costosa è: " + minima_chiave + " e costa " + str(dizionario[minima_chiave]) + " centesimi")


def merendina_meno_costosa_1_euro(dizionario):
    for chiave in dizionario:
        if dizionario[chiave] < 100:
            print("La merendina meno costosa è: " + chiave + " e costa " + str(dizionario[chiave]) + " centesimi")
            break


def merendina_meno_costosa_50_centesimi(dizionario):
    for chiave in dizionario:
        if dizionario[chiave] < 50:
            print("La merendina meno costosa è: " + chiave + " e costa " + str(dizionario[chiave]) + " centesimi")
            break


def merendina_meno_costosa_50_centesimi_lettere_pari(dizionario):
    for chiave in dizionario:
        if dizionario[chiave] < 50 and len(chiave) % 2 == 0:
            print("La merendina meno costosa è: " + chiave + " e costa " + str(dizionario[chiave]) + " centesimi")
            break


def merendina_meno_costosa_1_euro_lettere_pari(dizionario):
    for chiave in dizionario:
        if dizionario[chiave] < 100 and len(chiave) % 2 == 0:
            print("La merendina meno costosa è: " + chiave + " e costa " + str(dizionario[chiave]) + " centesimi")
            break


def main():
    distributore = {"merendine fiesta": 80, "merendine duplo": 90, "succhi di frutta": 45, "oreo": 90}
    merendina_piu_costosa(distributore)
    merendina_meno_costosa(distributore)
    merendina_meno_costosa_1_euro(distributore)
    merendina_meno_costosa_50_centesimi(distributore)
    merendina_meno_costosa_50_centesimi_lettere_pari(distributore)
    merendina_meno_costosa_1_euro_lettere_pari(distributore)


if __name__ == '__main__':
    main()