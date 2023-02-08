def scuola():

    print("La persona segue le elementari e le medie")
    n_bocciature = 0
    anno = 1
    risposta = ""
    print("Stai frequentando l'anno", anno, "di scuola")
    while(anno != 5 and n_bocciature < 3):
            if risposta == "si":
                n_bocciature += 1
            else:
                anno += 1
    return True