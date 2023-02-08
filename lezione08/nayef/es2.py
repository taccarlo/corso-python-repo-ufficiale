import random

min= int (input("inserisci min"))
max= int (input("inserisci max"))

list=[]

for x in range(20):
    list.append(random.randint(min,max))
print (list)

list.reverse()
print(list)

for x in range(len(list)):
    list[x]=list[x]*2
print(list)
