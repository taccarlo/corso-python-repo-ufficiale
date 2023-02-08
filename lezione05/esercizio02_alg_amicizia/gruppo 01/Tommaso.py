def incipit ():
    casa=str(input("è in casa?:"))
    if (casa == "sì" or casa == "Sì" or casa == "si" or casa == "Si" or casa == "SI"):
        risposta1=str(input("Ti va di mangiare qualcosa assieme?:"))
        if risposta1=="si":
            print("siete amici")
        elif risposta1=="no":
            bibita()
    elif casa=="no": 
        messaggio=str(input("Lascia un messaggio:"))
        print ("aspetta un messaggio")
        rmessaggio=input("messaggio: ")
        if rmessaggio=="si":
            print ("SIETE AMICI!:)")
        elif rmessaggio=="no":
            bibita()
def bibita():
    x = str(input(' E di bere qualcosa di caldo? '))
    if (x=="si"):
        risposta2=str(input('cosa preferisci bere: '))
        if(risposta2=='tea'):
            print('fatevi un tea e diventate amici')
        elif(risposta2=='caffè'):
            print('fatevi un caffè e diventate amici')
        elif(risposta2=='orangotango'):
            print('fatevi un orangotango e diventate amici')
    elif x=="no":
        funzione3()
def funzione3 ():
    print ("Allora svaghiamoci un po'")
    n=0
    while n<6:
        n+=1
        v=input("Cos'altro ti va di fare? ")
        y=input("è una cosa che piace anche a te? ")
        if y=="si":
            break
        elif y=="no": 
            continue
        else:
            print("<error>")
    if n==6:
        print ("Scegli fra tutte le opioni quella che ti sembra essere la meno disumana")
        print("Fattela piacere")
    else:
        print("e facciamolo insieme, dai..")
    print ("Svagatevi un po' insieme")  
incipit()