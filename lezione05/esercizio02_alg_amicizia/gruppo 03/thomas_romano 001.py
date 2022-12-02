def chiamare(amico):
    print('componi il numero di telefono')
    x=(input('sei a casa?'))
    if x=='sì':
    
        x= True
        x=(input('ti va di mangiare qualcosa?'))
        if x =='sì':
            x=True
        print(chiamare(True))   
    else:
        x=False
        print('gli lascio un messaggio')
      
        x=(input('controlliamo se mi ha richiamato'))
        if x == 'sì':
            x=True
            print('ascolto la risposta')
        else:
            x=False
        print('ok')
    return(True)
    print('siete diventati migliori amici')
print(chiamare(True))









