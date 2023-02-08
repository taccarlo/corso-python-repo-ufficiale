import os

def print_registro(registro):
  print(registro)


def aggiungi_studente(registro):
  newstud = input('Inserire il nuovo studente: ')
  registro[newstud] = 'none'


def aggiungi_voto(registro):
  stud = input('Inserire lo studente: ')
  voto = int(input('Inserire il nuovo voto: '))

  if(registro.get(stud) != None):
    registro[stud] = voto

def rimuovi_studente(registro):
  stud = input('Inserire lo studente da rimuovere: ')
  
  if(registro.get(stud) != None):
    del registro[stud]

os.system('cls')

registro = {}

aggiungi_studente(registro)
#aggiungi_voto(registro)
rimuovi_studente(registro)
print(registro)