import random

def smistamento(carte_in_mano):
    print("Carte: ")
    for x in range (2): 
        carte_in_mano.append(random.randint(1,13))
        if(carte_in_mano[x] == 1):
            carte_in_mano[x] = 'A'
        if(carte_in_mano[x] == 11):
            carte_in_mano[x] = 'J'
        if(carte_in_mano[x] == 12):
            carte_in_mano[x] = 'Q'
        if(carte_in_mano[x] == 13):
            carte_in_mano[x] = 'K'
        if(x == 0):
            print(carte_in_mano[x],end=' ')
        else:
            print(carte_in_mano[x])
    return carte_in_mano


def scelta(azione,carte_utente):
    if(azione == 1):
        x = random.randint(1,13)
        if(x == 1):
            carte_utente.append('A') 
        if(x == 11):
            carte_utente.append('J')
        if(x == 12):
            carte_utente.append('Q')
        if(x == 13):
            carte_utente.append('K')
    

