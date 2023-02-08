'''
Creare un programma che continua a chiedere all'utente una password finché l'utente non la indovina
'''

psw="cammello"
r=""

while(psw!=r):
    r=input("Inserire la password: ")
    if(psw!=r):
        print("Password svagliata")