"""
print a chunk of text
"""

import os
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
filename = askstring('Entry', 'Inserisci il nome del file di testo che vuoi leggere (senza estensione)')
numlines = askinteger('Entry', 'Inserisci il numero di righe del blocco')
with open('%s.txt' % filename, 'r') as file:
    text = file.read()

def more(text, numlines):
    lines = text.splitlines()
    chunk = lines[numlines:]
    print(chunk)

blocco = more(text, numlines)
print(blocco)
