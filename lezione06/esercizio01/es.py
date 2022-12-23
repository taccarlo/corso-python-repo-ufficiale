'''
#ES1
i=0
txt='{}° Andrea Lavagnoli'
for i in range(100):
    print(txt.format(i+1))
    i += 1
'''
'''
#ES2
i=0
for i in range(20):
    print(i+1)
    i += 1
'''
'''
#ES3
i=0
m=0
print("PARI")
for i in range(20):
    if (i%2==0):
        print(i)
    i += 1
print ("DISPARI")
for m in range(20):
    if (m%2!=0):
        print(m)
    m += 1
'''
'''
#ES4
txt='{}° Andrea Lavagnoli'
n =int(input('Inserisci un numero:'))
for i in range(10):
    if (n%3==0):
        print(txt.format(i+1))
    else:
        print("Non è dividibile per 3")
'''
#ES5
pwd =str(input('Inserisci una password:'))
while True:
    indovina =str(input('Prova ad indovinare la password:'))
    if (pwd == indovina):
        print('Hai indovinato')
        exit()
    else:
        print('La password non è giusta')