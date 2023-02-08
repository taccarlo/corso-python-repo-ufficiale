# inizializziamo il dizionario che contiene il prezzo delle merendine
snacks = {
    "fiesta": 80,
    "duplo": 90,
    "succo di frutta": 45,
    "oreo": 90
}

# funzione per acquistare una merendina
def buy_snack(snack, money):
    if snack in snacks:
        if money >= snacks[snack]:
            print("Hai acquistato una " + snack + " per " + str(snacks[snack]) + " centesimi")
            return money - snacks[snack]
        else:
            print("Non hai abbastanza denaro per acquistare una " + snack)
            return money
    else:
        print("La merendina selezionata non è disponibile")
        return money

# testiamo la funzione di acquisto
money = 500
money = buy_snack("fiesta", money)
money = buy_snack("oreo", money)
print("Ti rimangono " + str(money) + " centesimi")
