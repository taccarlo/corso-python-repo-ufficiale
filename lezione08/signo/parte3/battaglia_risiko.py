import es1

attacco = []
difesa = []

lose_attacco = 0
lose_difesa = 0

for i in range(3):
  attacco.append(es1.lancia_dado())

for i in range(3):
  difesa.append(es1.lancia_dado())

es1.ordina_dadi(attacco)
es1.ordina_dadi(difesa)

for i in range(2, -1, -1):
  print(difesa[i])
  if(es1.scontro(difesa[i], attacco[i])):
    lose_attacco += 1
  else:
    lose_difesa += 1

print(f"L'attaccante ha perso {lose_attacco} volte, {attacco}")
print(f"Il difensore ha perso {lose_difesa} volte, {difesa}")