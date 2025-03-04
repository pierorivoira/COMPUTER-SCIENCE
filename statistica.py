import dill, os, pickle
import pandas as pd
from tkinter.simpledialog import askstring
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI/DATA' % user)
filename = askstring('Entry', 'Inserisci il nome del file csv con i dati (senza estensione)')
#print('Your dataframe will be named <df>')
df = pd.read_csv('%s.csv' % filename)
print('Questa è la struttura dei tuoi dati:')
print(df.info())
column_name = askstring('Entry', 'Inserisci il nome della colonna che ti interessa') 
DATA = df['%s' % column_name]
def maxarray(dataframe):
	M = dataframe[0]
	for i in dataframe:
		if i > M:
			M = i
	return M
MAX = maxarray(DATA)
print('Il valore massimo della variabile <%s> è %f' % (column_name, MAX))

def minarray(dataframe):
	m = dataframe[0]
	for i in dataframe:
		if i < m:
			m = i
	return m
MIN = minarray(DATA)
print('Il valore minimo della variabile <%s> è %f' % (column_name, MIN))

DATA_ls = DATA.to_list()
SUM = 0
for i in range(len(DATA_ls)):
	SUM = SUM + DATA_ls[i]
AVERAGE = SUM / len(DATA_ls)
print('La media della variabile <%s> è %f' % (column_name, AVERAGE))
