
def incipit():
    print("funzione 1")
    return True
   
def offertaBevanda():
    print("offerta_bevanda")
    print("E di bere qualcosa di caldo?")
    risposta = input("si/no: ")
    if(risposta == "si"):
            scelta = input("Preferisci te, caffe o cioccolata? ")
            if(scelta == "tè"):
                print("Fatevi sto tè")
            elif(scelta == "caffè"):
                print("Fatevi sto caffè")
            elif(scelta == "cioccolata"):
                print("Fatevi sta cioccolata")
            print("Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
    if(risposta == 'no'):
        offertaAttivita()

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
        print('"Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa."')


incipit()
offertaBevanda()
offertaAttivita()


