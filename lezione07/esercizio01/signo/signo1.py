def sostituisci(arr, n1, n2):
  for i in range (len(arr)):
    arr[i] = n2 if arr[i] == n1 else arr[i]

  return arr

arr = [1, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n1 = 3
n2 = 4
print(arr)
print(sostituisci(arr, n1, n2))
  