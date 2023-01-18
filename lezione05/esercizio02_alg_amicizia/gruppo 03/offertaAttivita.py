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