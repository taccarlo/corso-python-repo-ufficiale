distributore = {
  'fiesta': 80,
  'duplo': 90,
  'succhi': 45,
  'oreo': 90
  }

print('Il prodotto più costoso è:', max(distributore, key = distributore.get))

for key in distributore:
  if(distributore[key] < 100 and len(key) % 2 == 0):
    print(key)

for key in distributore:
  if(distributore[key] < 50 or len(key) % 2 == 0):
    print(key)