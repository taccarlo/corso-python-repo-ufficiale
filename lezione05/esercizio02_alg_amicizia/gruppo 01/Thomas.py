def funzione_3 ():
    print ("Allora svaghiamoci un po'")
    n=0
    while n<6:
        n+=1
        x=input("Cos'altro ti va di fare? ")
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
print (funzione_3())

