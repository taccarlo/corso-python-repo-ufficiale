'''
Stampare a terminale per cento volte il vostro nome e il vostro cognome

Stampare a terminale tutti i numeri interi da 1 a 20

Stampare a terminale tutti i numeri pari da 1 a 20 e dopo tutti i numeri dispari da 1 a 20

Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, altrimenti stampa 10 volte la stringa “Non divisibile per 3” ( Consiglio: per conoscere se un numero è divisibile per un altro utilizzare l’operatore resto ‘%’ )

Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina
'''
'''
i=input("Nome e Cognome: ")
n=0
while (n < 100):
    n=n+1
    print (i,n)
'''

'''
for i in range (1, 20):
    i=i+1
    print (i)
'''
'''
for i in range (1, 20):
    i=i+1
    if (i%2==0):
        print (i)

for i in range (1, 20):
    i=i+1
    if (i%2!=0):
        print (i)
'''

'''
n=int(input("Inserisci un bel numero: "))
if (n%3==0):
    i=str("Tommaso Bendinelli")
    n=0
    while (n < 10):
        n=n+1
        print (i)
elif (n%3!=0):
    c="Non divisibile per 3"
    for c in range (10):
        print (c)
'''