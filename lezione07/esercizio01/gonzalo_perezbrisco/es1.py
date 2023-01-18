def sostituisci(a, v1, v2):
  for i in range(len(a)):
    if a[i]==v1:
      a[i]=v2
  print (a)
  
print(sostituisci(["p", "i", "p", "p", "o"], "p", "l"))