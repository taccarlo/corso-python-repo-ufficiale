'''
Stampare a terminale tutti i numeri pari da 1 a 20 e dopo tutti i numeri dispari da 1 a 20
'''

for x in range(1, 21):
    if(x%2==0):
        print(x)
        
for x in range(20):
    if(x%2!=0):
        print(x)