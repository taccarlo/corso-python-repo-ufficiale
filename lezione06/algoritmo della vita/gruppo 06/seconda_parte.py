def seconda_parte():
    n_p=0

    print("\nInizi a lavorare")
    for x in range(30):
        r=input("\nTi sei infortunato? ")
        if(r=="no"):
            n_p=terzo(n_p)
            if(n_p==3):
                print("\nSei diventato capo dell'azienda")
                break
        else:
            break