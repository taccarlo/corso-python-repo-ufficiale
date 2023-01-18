def check(arr):
  arr = list(dict.fromkeys(arr))
  return arr

arr = [1, 2, 2, 3, 2, 2, 3]
print(check(arr))