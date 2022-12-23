# Chiedere all'utente un numero da inserire,
# se questo è divisibile per 3 stampa per 10 volte 
# il tuo nome, altrimenti stampa 10 volte 
# la stringa “Non divisibile per 3”
a = int(input("Inserire un numero"))
b = 0
while(b<10):
    if(a%3==0):
        print("Carlo ciclo", b+1)
    else:
        print("Non divisibile per 3 ciclo",b+1)
    b+=1
    