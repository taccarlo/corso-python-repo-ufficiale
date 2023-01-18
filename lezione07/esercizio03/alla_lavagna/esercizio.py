'''
Si vuole creare un programma che riesca a gestire 
un registro che prevede coppie 
studente-voti e i voti sono una lista di interi. 
Scrivere queste funzioni:
chiedi_azione(): stampa 1 : aggiungi studente
			            2 : aggiungi voto a studente
                        3 : rimuovi studente
                        4 : visualizza registro
                        5 : esci
aggiungi_studente(): aggiunge uno studente al registro senza voti
aggiungi_voto(): chiede a quale studente aggiungere un voto e,
se esiste, lo fa
rimuovi_studente(): chiede quale studente eliminare dal registro,
 e se esiste lo fa
visualizza_registro(): stampa tutti gli studenti e tutti 
i loro voti
Infine scrivere un corpo principale che cicli fino a 
quando non viene scelto di uscire e che chieda quale 
azione eseguire.
'''
registro = {"paolo":[5,6] , "antonio":[], "giorgio":[]}
print("Benvenuto nel registro!")
def chiedi_azione():
    print ('premi 1 per aggiungere un utente\n premi 2 per rimuovere un utente\n premi 3 per visualizzare il registro\n premi 4 per aggiungere voto a studente')
    richiesta=input("scrivi il numero dell'azione: ")
    if richiesta=='1':
        aggiungi_studente()
    elif richiesta=='2':
        rimuovi_studente()
    elif richiesta=='3':
        visualizza_registro()
    elif richiesta== '4':
        aggiungi_voto()
    else:
        print('hai sbagliato')
def aggiungi_studente():
    nome_studente=input("inserisci nome:")
    registro[nome_studente]={}
def rimuovi_studente():
    x=input("utente da rimuovere:")
    if x in registro:
        registro.pop(x)
    else:
        print("ao, l'utente non v'è!")
def visualizza_registro():
    for x in registro:
        print("Nome alunno\\a:",x)
        print("voti:", registro[x])
def aggiungi_voto():
    nome=input("inserire nome dello studente")
    if nome in registro:
        voto=int(input("inserire il voto"))
        registro[nome].append(voto)
    else:
        print("Error")
while True:
    chiedi_azione()

