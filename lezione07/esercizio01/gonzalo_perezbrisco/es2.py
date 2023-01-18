def concatenare(a):
  s=""
  for i in range(len(a)):
    s+=str(a[i])
  return s
  
print(concatenare(["4", "3", "2", "1"]))