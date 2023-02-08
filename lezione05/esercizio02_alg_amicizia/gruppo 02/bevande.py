
risosposta=""

def bevande(a):
    if(a == "no"):
        print("E di bere qualcosa di caldo?")
        a = input("si/no: ")
        if(a == "si"):
            scelta = input("Preferisci tè, caffè o cioccolata? ")
            if(scelta == "tè"):
                print("Fatevi sto tè")
            elif(scelta == "caffè"):
                print("Fatevi sto caffè")
            elif(scelta == "cioccolata"):
                print("Fatevi sta cioccolata")
            print("Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
        elif(a == "no"):
            return "no"

rispsota_telefono =input()          
rispsota_attività = bevande(rispsota_telefono)

