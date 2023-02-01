import random

a= int(input("metti num"))

list=[]
for x in range(a):
    list.append(random.randint(-8,15))

max=max(list)
min=min(list)

print (max,min)
print (list)