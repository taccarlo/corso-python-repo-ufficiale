
lpari=[]
ldisp=[]
def funz01(lpari,ldisp):
    for x in range (1 , 100):
        if x % 2 == 0:
            lpari.append(x)
        elif x % 2 != 0 and x < 40 :
            ldisp.append(x) 
    
    while True:
        ris = input("PARI o DISPARI ? ->")
        if ris == "PARI":
            print(lpari)
            break
        elif ris == "DISPARI":
            print(ldisp)
            break
        else :
            print("scrivi PARI o DISPARI")

print(funz01(lpari ,ldisp))