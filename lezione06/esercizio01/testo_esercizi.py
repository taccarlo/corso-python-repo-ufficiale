
'''
Stampare a terminale per cento volte il vostro nome e il vostro cognome

Stampare a terminale tutti i numeri interi da 1 a 20

Stampare a terminale tutti i numeri pari da 1 a 20 e dopo tutti i numeri dispari da 1 a 20

Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, altrimenti stampa 10 volte la stringa “Non divisibile per 3” ( Consiglio: per conoscere se un numero è divisibile per un altro utilizzare l’operatore resto ‘%’ )

Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina

1
for i in range (100):
    i+=1
    print("Gabriele Segala")

2
for i in range (20):
    i+=1
    print(i)

3
i=0
while(i<20):
    i=i+2
    print(i)

i=1
while(i<20):
    print(i)
    i=i+2

4
num = int(input("inserici un numero: "))

if num%3==0:
    for i in range (10):
        print("Gabriele Segala")
        i+=1
else:
    for i in range (10):
        print("non è divisibile per 3")
        i+=1



password = "ciaoney"
str =input("Enter your password :")
while password!=str:
    print ("password non valida" )
    str =input("Enter your password :")

'''