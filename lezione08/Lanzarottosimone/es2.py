#creiamo una libreria di funzioni:

def lancio_dadi ():  #funzione che importa una funzione da libreria esterna per dare come output un numero casuale tra 1 e 6
    from random import randint
    return(randint(1,6))

def scontro (x,y):
    if x >= y:
        return True
    else:
        return False


def ordina_dadi(m): #ordina una lista in ordine decrescente
    list(m).sort(reverse=True)
    return m
    

    




    