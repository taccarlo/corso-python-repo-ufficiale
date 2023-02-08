#Stampare a terminale per cento volte il vostro nome e il vostro cognome
'''
for x in range(100):
    print("Er Pantera")
'''

#Stampare a terminale tutti i numeri interi da 1 a 20
'''
for x in range(20):
    print(x+1)
'''
#Stampare a terminale tutti i numeri pari da 1 a 20 e dopo tutti i numeri dispari da 1 a 20
'''
for x in range(21):
    if x%2==0:
        print(x)
for x in range(21):
    if x%2!=0:
        print(x)
'''

#Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, altrimenti stampa 10 volte la stringa “Non divisibile per 3” ( Consiglio: per conoscere se un numero è divisibile per un altro utilizzare l’operatore resto ‘%’ )
'''
if int(input("Inserisci un numero:"))%3==0:
    for x in range(10):
        print("Panterone")
else:
    for x in range(10):
        print("Num non divisibile per 3")
        '''

#Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina
passwd="roncstupido"
while True:
    if input("Indovina la password:")==passwd:
        break