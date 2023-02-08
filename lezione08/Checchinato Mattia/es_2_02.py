def most_expensive(snacks):
    most_expensive_snack = max(snacks, key=snacks.get)
    return most_expensive_snack

snacks = {
    "fiesta": 80,
    "duplo": 90,
    "succo di frutta": 45,
    "oreo": 90
}

print("La merendina più costosa è: " + most_expensive(snacks))
