
def incipit():
    input("Componi il numero di telefono della persona: ")
    print("E' in casa?")
    casa = input("si/no: ")
    if (casa == "no"):
        print("Lascia un messaggio \nAspetta di essere richiamato")
    elif(casa == "sì"):
        print("Ti va di mangiare qualcosa assieme?")
        risposta = input("ascolta la risposta: ")
        if(risposta == "si"):
            print("Mangiate qualcosa assieme")
            return True
        if(risposta == "No"):
            return False
            
def offertaBevanda():
    print("offerta_bevanda")
    print("E di bere qualcosa di caldo?")
    risposta = input("ascolta la risposta si/no: ")
    if(risposta == "si"):
            scelta = input("Preferisci te, caffe o cioccolata? ")
            if(scelta == "tè"):
                print("Fatevi sto tè")
            elif(scelta == "caffè"):
                print("Fatevi sto caffè")
            elif(scelta == "cioccolata"):
                print("Fatevi sta cioccolata")
            return True
    if(risposta == 'no'):
        offertaAttivita()

def offertaAttivita():
    print("Allora svaghiamoci un po'...")
    attivita = ""
    tipiace = "no"
    for x in range(6):
        attivita = input("Cos'altro ti va di fare?")
        tipiace = input("è una cosa che ti va di fare anche a te?")
        if(tipiace=="si"):
            print("e facciamolo dai...")
            break
    if(tipiace != "si"):
        print("Scegli fra tutte le opzioni quella che ti sembra la meno disumana")
        print("fattela piacere")
    print("svagatevi un po' insieme")
   
risp1 = incipit()
if(risp1==False):
    offertaBevanda()

print('"Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa."')


