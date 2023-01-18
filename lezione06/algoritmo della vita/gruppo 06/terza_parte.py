def terza_parte(n_promo):
    print("\nDevi continuare a lavorare")
    risposta=input("\nSei stato promosso? ")
    if(risposta=="si"):
        n_promo+=1
    return n_promo

print('La persona è nata!')
prima_parte()
print ('sei andato in pensione')
