# $ sudo apt install python3-tk
# script5.py

import os, sys
from tkinter.simpledialog import askstring

NOME = askstring('Entry', 'inserisci il tuo nome')
print(NOME)
COGNOME = askstring('Entry', 'inserisci il tuo cognome')
print(COGNOME)
ISTITUZIONE = askstring('Entry', 'inserisci il nome della tua istituzione')
print(ISTITUZIONE)
DOMINIO = askstring('Entry', "inserisci il dominio della tua istituzione, es. 'edu'")
print(DOMINIO)
ESTENSIONE = askstring('Entry', "inserisci l'estensione, es. 'it'")
print(ESTENSIONE)
indirizzo_1 = [NOME, COGNOME, ISTITUZIONE, DOMINIO, ESTENSIONE]
print(indirizzo_1)
NOME, COGNOME, ISTITUZIONE, DOMINIO, ESTENSIONE = range(5)
RUBRICA = (indirizzo_1)
indirizzo_completo_1 = RUBRICA[NOME] + '.' + RUBRICA[COGNOME] + '@' + RUBRICA[ISTITUZIONE] + '.' + RUBRICA[DOMINIO] + '.' +  RUBRICA[ESTENSIONE]

print(indirizzo_completo_1)

print(os.getlogin())
print(sys.platform)
