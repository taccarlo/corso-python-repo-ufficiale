#Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina
password = "pantera"

while True:
  pwd = input("Inserisci la password: ")
  if pwd == password:
    break
  else:
    print("Sbaià")

print("Brao mona")

