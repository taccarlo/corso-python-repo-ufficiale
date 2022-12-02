import sys
risposta = input("si/no ")
def attivita(risposta):
  if(risposta == "no"):
    n = 0
    x = input("Allora svaghiamoci un po'... \nCos'altro ti va di fare? ")
    voglia = input("E' una cosa che piace anche a me? si/no: ")
    while(n<5):
      n = n + 1
      if(voglia == "no"):
        x = input("Cos'altro ti va di fare? ")
        voglia = input("E' una cosa che piace anche a me? si/no: ")
      elif(voglia == "si"):
        print("E facciamolo insieme, dai... \nSvagatevi un po' insieme")
        print("Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
        sys.exit()
      print("Scegli fra tutte le opzioni quella che ti appare meno disumana \nFattela piacere \nSiete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa.")
print(attivita(risposta))