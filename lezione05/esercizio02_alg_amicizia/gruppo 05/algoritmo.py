print("Componi il numero di telefono della persona \nE' in casa?")
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
    elif(risposta == "no"):
        print("E di bere qualcosa di caldo?")
        risposta = input("si/no: ")
        if(risposta == "si"):
            scelta = input("Preferisci te', caffè o cioccolata? ")
            if(scelta == "te'"):
                print("Fatevi sto te'")
            elif(scelta == "caffè"):
                print("Fatevi sto caffè")
            elif(scelta == "cioccolata"):
                print("Fatevi sta cioccolata")
            print("Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
        elif(risposta == "no"):
            n = 0
            print("Allora svaghiamoci un po'...")
            print("Cos'altro ti va di fare?")
            voglia = input("E' una cosa che piace anche a me? si/no: ")
            while(voglia == "no" and n<5):
                n = n + 1
                print("Cos'altro ti va di fare?")
                voglia = input("E' una cosa che piace anche a me? si/no: ")
                if(voglia == "si"):
                    print("E facciamolo insieme, dai... \nSvagatevi un po' insieme")
                    print("Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
                    sys.exit()
            print("Scegli fra tutte le opzioni quella che ti appare meno disumana \nFattela!")