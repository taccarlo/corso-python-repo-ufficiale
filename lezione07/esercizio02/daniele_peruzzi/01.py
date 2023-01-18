list = [1, 2, 2, 3, 2, 2, 3]

def noDuplicates(list):
    m = -1
    for x in range(len(list)-1):
        m+=1
        if list[m] == list[m+1]:
            del list[m]
            m-=1
    return list

print(noDuplicates(list))