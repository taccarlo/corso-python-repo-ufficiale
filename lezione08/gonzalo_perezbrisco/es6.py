def trova(d):
  return (max(d, key=d.get))

def seconda(d):
  tmp = {}
  for key in d:
    if(len(key)%2==0):
      if(d[key]<100):
        tmp.update({key: d[key]})
  return tmp

def terza(d):
  tmp = {}
  for key in d:
    if(d[key]<50) or (len(key)%2==0):
      tmp.update({key: d[key]})
  return tmp

distribuitore = {"merendine fiesta": 80, "merendine duplo": 90, "succhi di frutta": 45, "oreo": 90}
print(trova(distribuitore))
print(seconda(distribuitore))
print(terza(distribuitore))