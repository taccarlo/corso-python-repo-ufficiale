#Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina


pwd = input("Inserisci la password: ")
while pwd != "password":
    pwd = input("Password errata, inserisci la password: ")
print("Password corretta")

