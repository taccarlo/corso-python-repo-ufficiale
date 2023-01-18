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



registro = {"paolo":[] , "antonio":[], "giorgio":[]}
print("Benvenuto nel registro!")

def chiedi_azione():
    print("1 : aggiungi studente")
    print("2 : aggiungi voto a studente")
    print("3 : rimuovi studente")
    print("4 : visualizza registro")
    print("5 : esci")
    return int(input("Quale azione vuoi eseguire? "))
def aggiungi_studente():
    nome = input("Inserisci il nome dello studente: ")
    if nome in registro:
        print("Lo studente è già presente nel registro")
    else:
        registro[nome] = []
        print("Lo studente è stato aggiunto al registro")
def aggiungi_voto():
    nome = input("A quale studente vuoi aggiungere un voto? ")
    if nome in registro:
        voto = int(input("Inserisci il voto: "))
        registro[nome].append(voto)
        print("Il voto è stato aggiunto al registro")
    else:
        print("Lo studente non è presente nel registro")
def rimuovi_studente():
    nome = input("Qual è il nome dello studente da rimuovere? ")
    if nome in registro:
        del registro[nome]
        print("Lo studente è stato rimosso dal registro")
    else:
        print("Lo studente non è presente nel registro")
def visualizza_registro():
    for nome in registro:
        print(nome, registro[nome])
while True:
    azione = chiedi_azione()
    if azione == 1:
        aggiungi_studente()
    elif azione == 2:
        aggiungi_voto()
    elif azione == 3:
        rimuovi_studente()
    elif azione == 4:
        visualizza_registro()
    elif azione == 5:
        break
    else:
        print("Azione non valida")

    