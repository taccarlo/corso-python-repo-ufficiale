for i in range (0,100):
    print ("il vostro nome e il vostro cognome")
n=1
while n<21:
    print (n)
    n=n+1

m=1
o=1
while m<21:
    if m%2 == 0:
        print(m)
    m=m+1
while m>=20 and m<40 and o<20:
    print (o)
    m=m+1
    o=o+2
    
p=int(input("inserisci numero:"))
if p%3 == 0:
    for i in range (10):
        print("il tuo nome")
else:
    for i in range (10):
        print("Non divisibile per 3")

password="wordpass"

a=input("inserisci password:")

while a != password :
    a=input("inserisci password:")
    
