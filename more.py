"""
split and interactively page a string or file of text
"""

import os
from tkinter.simpledialog import askinteger, askstring
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
filename = askstring('Entry', 'Inserisci il nome del file di testo che vuoi leggere (senza estensione)')
numlines = askinteger('Entry', 'Inserisci il numero di righe del blocco')
with open('%s.txt' % filename, 'r') as file:
    text = file.read()

def more(text, numlines):
    lines = text.splitlines()
    while lines:
    	chunk = lines[:numlines]
    	lines = lines[numlines:]
    	for line in chunk: print(line)
    	if lines and input('More?') not in ['y', 'Y']: break

more(text, numlines)
