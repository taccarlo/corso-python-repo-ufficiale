#Chiedere all'utente un numero da inserire, se questo è divisibile per 3 stampa per 10 volte il tuo nome, 
# altrimenti stampa 10 volte la stringa “Non divisibile per 3” 
# Chiedi all'utente di inserire un numero
numero = int(input("Inserisci un numero: "))
if numero % 3 == 0:
  for i in range(10):
    print("Alessandro")
else:
  for i in range(10):
    print("")
