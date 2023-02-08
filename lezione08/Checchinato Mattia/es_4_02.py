def find_snacks(snacks):
    for snack, price in snacks.items():
        if price < 50 | len(snack) % 2 == 0:
            print("La merendina " + snack + " costa " + str(price) + "meno di 50 centesimi e ha un numero di lettere pari nel nome")

snacks = {
    "fiesta": 80,
    "duplo": 90,
    "succo di frutta": 45,
    "oreo": 90
}

find_snacks(snacks)