def incipit():
    print("funzione 1")
    return True
def offertaBevanda():
    print("funzione 2")
    return True
def offertaAttivita():
    n=0
    print("Allora svaghiamoci un po'...")
    r="no"
    while(n > 6 and r = "no"):
        risposta = input("Cos'altro ti va di fare?")
        siono = input("è una cosa che va di fare anche a te?")
        if(siono == "si"):
            print("E facciamolo insieme,dai...")
            print("Ci svaghiamo insieme")
            print("Siamo diventati amici!")
            return
        else:
            n=n+1
    risposta = input("Scegli fra tutte le opzioni quella che ti sembra essere la meno disumana")
    print("fattela piacere")
    print("Ci svaghiamo insieme")
    print("Siamo diventati amici!")    
    return





incipit()
offertaBevanda()
offertaAttivita()

