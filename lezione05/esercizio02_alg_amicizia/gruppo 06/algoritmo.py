def incipit():
    input("Componi il numero di telefono della persona: ")
    print("E' in casa?")
    casa = input("si/no: ")
if (casa == "si"):
    print("sus")
elif(casa == "no"):
    print("Lascia un messaggio \nAspetta di essere richiamato")
    print("Ti va di mangiare qualcosa assieme?")
    risposta = input("si/no: ")
    if(risposta == "si"):
        print("Mangiate qualcosa assieme")
        print("Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
    
   
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


