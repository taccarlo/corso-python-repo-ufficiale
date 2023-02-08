print ("ALGORITMO DELLA VITA!!\n\nÈ NATO!!")
print ("FA LE ELEMENTARI\nFA LA MEDIE\nINIZIA LE SUPERIORI.....")

def scuola ():
    promozione=0
    bocciatura=0
    while (promozione<5 and bocciatura<3):
        promozione=promozione+1
        promozione1=input("È stato promosso??:")
        if (promozione1=="no"):
            promozione=promozione-1
            bocciatura=bocciatura+1
            print ("IL POLLO È STATO BOCCIATO")
        elif(promozione1=="si"):
            print("ANNO", promozione,"PASSATO!!")
            
def lavoro ():
    print("E ORA INIZIA A LAVORARE")
    servizio=0
    while (servizio<30):
        servizio=servizio+1
        print(servizio,"° ANNO DI SERVIZIO ZIO PERA!!")
    infortunio=input("INFORTUNIO DEBILITANTE??:")
    if (infortunio=="si"):
        print ("PENSIONE D'INVALIDITÀ")
    elif(infortunio=="no"):
        promozione()

def promozione():
    promozione2=0
    while (promozione2<3):
        promozione2=promozione2+1
        promozione1=input("È stato promosso??:")
        if (promozione1=="no"):
            promozione2=promozione2-1
        elif(promozione1=="si"):
            print("PROMOSSOOO!!")
    print("CAPO D'AZIENDA ZIO CAN\nE VA PURE IN PENSIONE LA BESTIA")
            
scuola ()
lavoro ()