#Stampare i numeri pari da 1 a 100,
 #poi stampare i numeri dispari da 1 a 40
#(utilizzando il ciclo for con la funzione range)
for i in range (2,101,2):
    print(i)
for n in range (1,101,2):
    print(n)
#Generare una lista lunga 20 di numeri casuali compresi 
#tra n ed m inseriti da utente, a questo punto stampare
#la lista e successivamente stamparla capovolta 
#(dall’ultimo elemento al primo) e raddoppiando ogni 
#numero 
import random
k=[]
n=int(input("a:"))
m=int(input("b:"))
for i in range(20):
    l=random.randint(n,m)
    k.append(l)
print(k)

i=-1
e=[]
for x in range(len(k)):
    e.append(k[i]*2)
    i-=1
print(e)    
#Scrivere un programma che individui il valore 
#massimo e minimo all’interno di una lista lunga
#n (inserito da utente) di numeri generati casualmente 
#da -8 a 15.
q=[]
f=int(input("numero:"))
for l in range (f):
    l=random.randint(-8,16)
    q.append(l)
print(q)
print(max(q)," ",min(q))