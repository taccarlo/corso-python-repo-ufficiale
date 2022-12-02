def incipit ():
    casa=str(input("è in casa?:"))
    if (casa == "sì" or casa == "Sì" or casa == "si" or casa == "Si" or casa == "SI"):
        risposta1=str(input("Ti va di mangiare qualcosa assieme?:"))
        if (risposta1 == "sì" or risposta1 == "Sì" or risposta1 == "si" or risposta1 == "Si" or risposta1 == "SI" or risposta1 == "ok" or risposta1 == "Ok" or risposta1 == "OK"):
            print("SIETE AMICI!!!")
        else:
            bevanda=str(input("BEVIAMO?:"))
        
    else: 
        messaggio=str(input("Lascia un messaggio:"))
        
print (incipit ())