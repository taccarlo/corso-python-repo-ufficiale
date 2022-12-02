def offertaAttivita():
    print("funzione 3")
    return
def offertaBevanda():
    risposta=input("e di bere qualcosa?")
    if (risposta == "si"):
        print("Scegli:")
        print("tè")
        print("caffè")
        print("cioccolata")
        risposta=input("")
    else:
        offertaAttivita()
    return True
def incipit():
    numero=("\nComponi il numero di telefono: ")
    risposta=("\nE' a casa? ")
    print("\nLasci un messaggio e aspetti di essere richiamato...")
    risposta=("\nTi va di mangiare qualcosa assieme? ")
    if(risposta=="si"):
        print("\nMangiate qualcosa assieme")
    elif(risposta=="no"):
        offertaBevanda()
    return True
incipit()
offertaAttivita()
print("SIETE DIVENTATI AMICI!!")
