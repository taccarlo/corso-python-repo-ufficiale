def prima_parte():
    n_bocciature=0
    numero_anno=0

    print("La persona segue le elementari")
    while((numero_anno<5) and (n_bocciature<3)):
        print(numero_anno+1, "° delle superiori")
        risposta=input("Sei stato bocciato?")
        if(risposta=="si"):
            n_bocciature = n_bocciature+1
        else:
            numero_anno = numero_anno+1
    seconda_parte()


def seconda_parte():
    n_promo=0

    print("\nInizi a lavorare")
    for x in range(30):
        risposta=input("\nTi sei infortunato? ")
        if(risposta=="no"):
            n_promo=terza_parte(n_promo)
            if(n_promo==3):
                print("\nSei diventato capo dell'azienda")
                break
        else:
            break
        
def terza_parte(n_promo):
    print("\nDevi continuare a lavorare")
    risposta=input("\nSei stato promosso? ")
    if(risposta=="si"):
        n_promo+=1
    return n_promo

print('La persona è nata!')
prima_parte()
print ('sei andato in pensione')
