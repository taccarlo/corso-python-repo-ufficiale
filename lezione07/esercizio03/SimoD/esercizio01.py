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

def chiedi_azione():
    print("1 : aggiungi studente \n2 : aggiungi voto a studente \n3 : rimuovi studente \n4 : visualizza registro \n5 : esci")
