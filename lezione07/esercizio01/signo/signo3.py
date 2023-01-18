def check(arr):
  temp = 0

  for i in range(len(arr)):
    if (not(isinstance(arr[i], int))):
      temp += 1
      break
    
  if temp == 0:
    return [min(arr), sum(arr)/len(arr), max(arr)]
  else:
    return 'error'


arr = [1, 2, 3, 4, 5, 6, 7, 'a', 9, 10, 11, 12, 13, 14]
print(check(arr))
