def incipit():
    print("funzione 1")
    return True
def offertaBevanda():
    print("offerta_bevanda")
    return True
def offertaAttivita():
    print("Allora svaghiamoci un po'...")
    attivita = ""
    for x in range(6):
        attivita = input("Cos'altro ti va di fare?")
        tipiace = input("è una cosa che ti va di fare anche a te?")
        if(tipiace=="si"):
            print("e facciamolo dai...")
            print("svagatevi un po' insieme")
            return
    print("Scegli fra tutte le opzioni quella che ti sembra la meno disumana")
    print("fattela piacere")
    print("svagatevi un po' insieme")

incipit()
offertaBevanda()
offertaAttivita()


