list = ["c", "i", "a", "o"]

def toString(list):
    str = ""
    for x in range(len(list)):
        str += list[x]
    return str

print("Lista concatenata:", toString(list))