print("La persona è nata!")



def infortunio():

    counter_anni =0
    
    while counter_anni <=30:
    
        print(counter_anni)
    
        counter_anni += 1
    
    import random

    casuale = random.randrange(1,60)

    if casuale <=30:
        print('hai la pensione')
    else:
        print('nessun infortunio')
    lavoro.py

def scuola():

    print("La persona segue le elementari e le medie")
    n_bocciature = 0
    anno = 1
    risposta = ""
    print("Stai frequentando l'anno", anno, "di scuola")
    while(anno != 5 and n_bocciature < 3):
            risposta = input("Sei stato bocciato?")
            if risposta == "si":
                n_bocciature += 1
            else:
                anno += 1
    infortunio()

scuola()