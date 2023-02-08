'''
Stampare a terminale per cento volte il vostro nome e il vostro cognome'''
nome=input("inserire il vostro nome")
i=1
while i<=100 :
    print(nome , i)
    i+=1
'''

Stampare a terminale tutti i numeri interi da 1 a 20'''
for (x) in range(1,21):
    print (int(x))

'''Stampare a terminale tutti i numeri pari da 1 a 20 e dopo tutti i numeri dispari da 1 a 20'''
print("ecco i numeri pari")
for x in range (1, 21):
    if x%2==0:
        print(x)
print("ecco i numeri dispari ")
for x in range (1, 21):
    if x%2!=0:
        print(x)
'''Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, altrimenti stampa 10 volte
 la stringa “Non divisibile per 3” ( Consiglio: per conoscere se un numero è divisibile per un altro utilizzare l’operatore resto ‘%’ )'''
n=input(("inserire un numero "))
if int(n)%3!=0:
    for x in range(11):
        print("non dividibile per 3")
else:
    for x in range(11):
        print(nome)
'''Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina
'''
password="lanza"
while True :
    pswd=input("inserire password")
    if pswd==password:
        break
    