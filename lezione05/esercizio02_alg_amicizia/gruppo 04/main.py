def offertaAttivita():
    n=0
    print("Allora svaghiamoci un po'...")
    r="no"
    while((n < 6) and (r == "no")):
        r = input("Cos'altro ti va di fare?")
        r = input("è una cosa che va di fare anche a te?")
        if(r == "si"):
            print("E facciamolo insieme,dai...")
            print("Ci svaghiamo insieme")
            return
        else:
            n=n+1
    r = input("Scegli fra tutte le opzioni quella che ti sembra essere la meno disumana")
    print("fattela piacere")
    print("Ci svaghiamo insieme")

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

def incipit():
    numero=input("\nComponi il numero di telefono: ")
    risposta=input("\nE' a casa? ")
    if (risposta == "no"):
        print("\nLasci un messaggio e aspetti di essere richiamato...")
    risposta=input("\nTi va di mangiare qualcosa assieme? ")
    if(risposta=="si"):
        print("\nMangiate qualcosa assieme")
    elif(risposta=="no"):
        offertaBevanda()

incipit()

print("SIETE DIVENTATI AMICI!!")
