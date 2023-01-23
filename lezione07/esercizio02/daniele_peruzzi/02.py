def sortAscendent(list1, list2):
    list1 = list1 + list2
    list1.sort()
    return list1

print(sortAscendent([1,2,2,3,2,2,3],[1,2,3,2,3]))