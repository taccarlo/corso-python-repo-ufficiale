def si_no(r):
    print("\n", r)
    while ((r != "si") and (r != "no")):
        r = input("")
        if(r != "si") and (r != "no"):
            print("\nRispondere 'si' o 'no'")
    return r

t = input("Inserire numero di telefono della persona: ")   
r = si_no("E' in casa?")

if(r == "no"):
    print("\nLasci un messsaggio e aspetti risposta")
    
r = si_no("Ti va di manggiare qualcosa insieme?")
if(r == "si"):
    r = 1
elif(r == "no"):
    r = si_no("E di bere qualcosa di caldo?")
    if(r == "si"):
        print("\nScegli:\n1) Tè\n2) Caffè\n3) Cioccolata\n")
        while((r != "1") and (r != "2") and (r != "3")):
            r = input("")
            if(r != "1") and (r != "2") and (r != "3"):
                print("\nRispondere 1, 2 o 3")
        r=1
    elif(r == "no"):
        a = []
        print("\nCosa mi piacerebbe fare (Scrivere 'basta' quando hai finito): ")
        while((r != "basta") and (r != 1)):
            r = input("")
            if(r != "basta"):
                s = si_no("E' una cosa che piace fare anche a te?")
                if(s == "si"):
                    r = 1
                elif(s == "no"):
                    a.append(r)
                    print("\nScrivi un'altra proposta")
        if(r == "basta"):
            for x in range(len(a)):
                print("\n", x+1, ") ", a[x])
            print("\nScegli l'opzione meno disumana e fattela piacere")
            r=0
            while ((1 > r) or (r > len(a))):
                r = int(input("\n"))
                if((1 > r) or (r > len(a))):
                    print("\nScegliere un numero tra 1 e", len(a))
                else:
                    r = 1
if (r == 1):
    print("\n\n\nSiete diventati amici!!!")