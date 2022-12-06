def prima_parte():
    n_bocciature=0
    numero_anno=0

    print("La persona è nata!")
    print("La persona segue le elementari")
    while((numero_anno<5) and (n_bocciature<3)):
        print(numero_anno+1, "° delle superiori")
        risposta=print("Sei stato bocciato?")
        if(risposta=="si"):
            n_bocciature = n_bocciature+1
        else:
            numero_anno = numero_anno+1
    seconda_parte()
        
        
