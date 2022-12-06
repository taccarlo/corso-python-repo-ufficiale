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