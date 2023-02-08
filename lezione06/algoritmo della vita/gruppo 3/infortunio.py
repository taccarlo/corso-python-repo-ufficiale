def infortunio(persona):

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