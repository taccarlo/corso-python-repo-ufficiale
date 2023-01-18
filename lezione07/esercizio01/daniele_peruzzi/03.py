list = [1, 2, 3, 4]

def somma(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum

def media(list):
    return somma(list)/len(list)

def max(list):
    max = list[0]
    for x in range(len(list)):
        if list[x] > max:
            max = list[x]
    return max

def min(list):
    min = list[0]
    for x in range(len(list)):
        if list[x] <= min:
            min = list[x]
    return min

def noString(list):
    for x in range(len(list)):
        if type(list[x]) != int:
            return "Error"
        else:
            result = [min(list), media(list), max(list)]
            return result

print(noString(list))