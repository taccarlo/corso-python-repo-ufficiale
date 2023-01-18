print("Crea una lista: (quit per uscire-swap per cambiare 2 posizioni)")
list=[]
i=True

def swapIndex(list, a, b):
    for x in range(len(list)):
        if a in list:
            list.insert(list.index(a),b)
            list.remove(a)
    return list

while i==True:
    x=input()
    if x=="quit":
        print(list)
        i=False
    elif x=="swap":
        print("Indica quali valori vuoi swappare:")
        first_element = input()
        second_element = input()
    else: list.append(x)

print("La lista swappata:",swapIndex(list,first_element,second_element))