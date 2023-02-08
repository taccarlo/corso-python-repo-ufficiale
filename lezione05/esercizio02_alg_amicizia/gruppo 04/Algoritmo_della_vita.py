def pensione():
    return
def lavoro():
    anni_di_servizio = 1
    while(anni_di_servizio < 31):
        anni_di_servizio+=1
        print("anno di servizio")
    return
def scuola():
    print("la persona segue le elementari e medie")
    n_bocciature = 0
    anno_numero = 1
    p = 0
    while(anno_numero < 7):
        if(p == 5 or n_bocciature == 3):
            lavoro()
            return
        
        risposta = input("inserire P se promosso o B se bocciato \n")


        if(risposta == "P" or risposta == "p"):
            print("è stato promosso")
            p +=1
            anno_numero+=1

        if(risposta == "B" or risposta == "b"):
            print("è stato bocciato")
            n_bocciature+=1
            anno_numero+=1
    return

scuola()
lavoro()