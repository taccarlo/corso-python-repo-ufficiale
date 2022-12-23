'''
Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, altrimenti stampa 10 volte la stringa “Non divisibile per 3” ( Consiglio: per conoscere se un numero è divisibile per un altro utilizzare l’operatore resto ‘%’ )
'''

n=int(input("Inserire un numer: "))

if(n%3==0):
    for x in range(10):
        print("Gonzalo Perez Brisco")
else:
    for x in range(10):
        print("Non divisibile per 3")