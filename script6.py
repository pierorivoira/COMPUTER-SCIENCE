# $ sudo apt install python3-tk
# script5.py

import os, sys
from tkinter.simpledialog import askstring, askinteger
NOME = []
COGNOME = []
ISTITUZIONE = []
DOMINIO = []
ESTENSIONE = []
INDIRIZZO = []
INDIRIZZO_COMPLETO = []
RUBRICA = []
CONTATORE = askinteger('Entry', 'inserisci il numero di indirizzi')
for i in range(CONTATORE):

	nome = askstring('Entry', 'inserisci il tuo nome')
	print(nome)
	NOME.append(nome)
	cognome = askstring('Entry', 'inserisci il tuo cognome')
	print(cognome)
	COGNOME.append(cognome)
	istituzione = askstring('Entry', 'inserisci il nome della tua istituzione')
	print(istituzione)
	
	DOMINIO[i] = askstring('Entry', "inserisci il dominio della tua istituzione, es. 'edu'")
	print(DOMINIO[i])
	ESTENSIONE[i] = askstring('Entry', "inserisci l'estensione, es. 'it'")
	print(ESTENSIONE[i])
	INDIRIZZO[i] = [NOME[i], COGNOME[i], ISTITUZIONE[i], DOMINIO[i], ESTENSIONE[i]]
	print(INDIRIZZO[i])
	NOME[i], COGNOME[i], ISTITUZIONE[i], DOMINIO[i], ESTENSIONE[i] = range(5)
	RUBRICA.append = (INDIRIZZO[i])
	print(RUBRICA)
#	INDIRIZZO_COMPLETO[i] = RUBRICA[0][NOME] + '.' + RUBRICA[0][COGNOME] + '@' + RUBRICA[0][ISTITUZIONE] + '.' + RUBRICA[0][DOMINIO] + '.' +  RUBRICA[0][ESTENSIONE]



print(os.getlogin())
print(sys.platform)
