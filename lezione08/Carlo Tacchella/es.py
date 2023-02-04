dizionario = {
    "fiesta":80,
    "duplo":90,
    "succhi di frutta":45,
    "oreo":90
    }

def piu_costoso(a):
    return max(a, key=a.get)

def fun_1(a):
    dict = {}
    for item in a:
        if len(item)%2==0 and a[item]<100:
            dict[item]=a[item]
    return dict 

def fun_2(a):
    dict = {}
    for item in a:
        if len(item)%2==0 or a[item]<50:
            dict[item]=a[item]
    return dict 

print("il più costoso è ", piu_costoso(dizionario))
print(fun_1(dizionario))
print(fun_2(dizionario))
