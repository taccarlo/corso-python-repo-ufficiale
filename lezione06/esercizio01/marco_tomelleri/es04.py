'''Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, altrimenti stampa 10 volte la stringa “Non divisibile per 3” ( Consiglio: per conoscere se un numero è divisibile per un altro utilizzare l’operatore resto ‘%’ )
'''
num = int(input("Inserisci un numero: "))
if num%3==0:
    for i in range(10):
        print("marco")
else:
    for i in range(10):
        print("Non divisibile per 3")


