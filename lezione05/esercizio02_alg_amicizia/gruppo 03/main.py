
def chiamare():
    
    input("Componi il numero di telefono")  
    x=input("Sei a casa?")
    if x=='no': 
        input('Gli lascio un messaggio')
        print("Aspetta di essere richiamato")
    x=input("Ti va di mangiare qualcosa assieme?")
    if x=="no":
        offertabevanda()
    else:
        print("Mangiamo qualcosa assieme")
    
def offertabevanda():
    y=input("bevi qualcosa di caldo? ")
    if y=="si":
        print("vuoi tè, caffè o cioccolata")
        o=input("quale preferisci? ")
        if o=="tè":
          print("facciamoci sto tè")
        elif o=="caffè":
          print("facciamoci sto caffè")
        elif o=="cioccolata":
          print("facciamoci sta cioccolata")
        print("SIETE DIVENTATI AMICI \nora hai una persona in più a cui \npoter rompere le palle \nin caso di bisogno e viceverso")
    else:
       offertaAttività()

def offertaAttività():
    print("Allora svaghiamoci un pò...")
    attività = ""
    for x in range(6):
        attività = input("Cos'altro ti va di fare?")
        risposta = input("è una cosa che ti va di fare anche a te?")
        if(risposta=="si"):
            print("e facciamolo dai...")
            print("svagatevi un po' insieme")
            return
    print("Scegli fra tutte le opzioni quella che ti sembra la meno disumana")
    print("fattela piacere")
    print("svagatevi un po' insieme")
    print("Siamo diventati amici")

chiamare()