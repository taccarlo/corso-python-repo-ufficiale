'''
Creare una funzione con tre input che mi calcoli la media
 e restituisca il valore

'''
def media (n1,n2,n3):
    media_n = ((n1+n2+n3)/3)
    print(media_n)
    return()

n1 = int(input("Inserisci un numero:"))
n2 = int(input("Inserisci un altro numero:"))
n3 = int(input("Inserisci un altro numero:"))
m = media(n1,n2,n3)