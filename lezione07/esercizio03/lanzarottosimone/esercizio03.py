registro = {"paolo":[] , "antonio":[], "giorgio":[]}
print("Benvenuto nel registro!")
print("1 -> aggiungi studente , 2 ->rimuovi studente, 3-> visualizza registro, 4-> esci ")
def chiedi_azione(registro):
    azione=int(input("inserisci un azione: "))
    if azione == 1:
        aggiungi_studente(registro)
    elif azione == 2:
        rimuovi_studente(registro)
    elif azione == 3:
        visualizza_registro(registro)
    elif azione == 4:
        print("esci")
        

def aggiungi_studente(registro):
    nome=input("nome studente")
    voto=input("voto studente")
    registro[nome]=voto
    return registro
def rimuovi_studente():
    nome_r=input("nome utente")
    if nome_r in registro:
        registro.pop(nome_r)
    return registro
def visualizza_registro(registro):
    for x in registro:
        y= registro.get(x)
        print(x ,y  )
    return registro

print (chiedi_azione(registro))
