#Stampare a terminale tutti i numeri pari da 1 a 20 e dopo tutti i numeri dispari da 1 a 20
for i in range(1, 21):
  if i % 2 == 0:
    print(i)

for i in range(1, 21):
  if i % 2 != 0:
    print(i)