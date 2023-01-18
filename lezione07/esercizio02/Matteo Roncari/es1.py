lis = []
lunghezza = int(input('Inserire la lunghezza della lista '))
for x in range(lunghezza):
    lis.append(input(f'Inserisci il {x} valore '))
print(lis)
i = 0
j = len(lis)
while i < j:
    if i >=1 and lis[i] == lis[i-1]:
        lis.pop(i)
        j = len(lis)
    i += 1
print(lis)