def controllo(a):
  min = a[0]
  max = a[0]
  media = a[0]
  for i in range(1, len(a)):
    if not type(a[i]) == int:
      return "error"
    else:
      if a[i] < min:
        min = a[i]
      if a[i] > max:
        max = a[i]
      media += a[i]
      
  return ([min, media/len(a), max])
  
print(controllo([1, 2, 3, 4, 5]))