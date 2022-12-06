def lavoro():
    n_promozioni=0 
    while n_promozioni<3:
        x=input("hai ottenuto una promozione? ")
        if x=="si":
         print("sei stato promosso")
         n_promozioni+=1
        elif x=="no":
         print("continua a lavorare")
    print("sei divventato capo di azienda \npuoi andare in pensione")