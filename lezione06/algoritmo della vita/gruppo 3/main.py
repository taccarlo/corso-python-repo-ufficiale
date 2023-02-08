print("La persona è nata!")

def lavoro():
    n_promozioni=0 
    while n_promozioni<3:
        x=input("hai ottenuto una promozione? ")
        if x=="si":
         print("sei stato promosso")
         n_promozioni+=1
        else:
            print("continua a lavorare")
    print("sei diventato capo di azienda \npuoi andare in pensione")

def infortunio():
    import random
    counter_anni = 1
    casuale = random.randrange(1,100)

    while counter_anni <=30:
        print(counter_anni)
        if casuale <=30:
            print("Anno infortunio:", casuale)
            print('hai la pensione')
            return
        counter_anni += 1
    if counter_anni==30:
        print("Nessun infortunio")
    lavoro()

def scuola():

    print("La persona segue le elementari e le medie")
    n_bocciature = 0
    anno = 1
    print("Stai frequentando l'anno", anno, "di scuola")
    while(anno != 5 and n_bocciature < 3):
            risposta = input("Sei stato bocciato?")
            if risposta == "si":
                n_bocciature += 1
            else:
                anno += 1
    infortunio()

scuola()