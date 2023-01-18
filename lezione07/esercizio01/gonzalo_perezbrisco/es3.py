def controllo(a):
  for i in range(1, len(a)):
    if not type(a[i]) == int:
      return "error"
      
  return ([min(a), sum(a)/len(a), max(a)])
  
print(controllo([1, 2, 3, 4, 5]))