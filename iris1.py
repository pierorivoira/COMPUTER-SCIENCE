# iris1.py

import os
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
# os.system('sudo apt-get install python3-sklearn python3-sklearn-lib python-sklearn-doc')
import pandas as pd
from tkinter.simpledialog import askfloat
from sklearn import svm, datasets
#os.system('mkdir COMPUTER_SCIENCE')
#os.chdir('/home/%s/COMPUTER_SCIENCE' % user)
#os.system('mkdir AI')
#os.chdir('AI')

os.system('wget wget https://raw.githubusercontent.com/pierorivoira/COMPUTER-SCIENCE/refs/heads/main/iris.csv')
print('Ho scaricato il file <iris.csv> da https://github.com/pierorivoira/COMPUTER-SCIENCE')
iris_df = pd.read_csv('iris.csv')
iris_df = iris_df.rename(columns={'sepal_length': 'SEPAL LENGTH'})
iris_df = iris_df.rename(columns={'sepal_width': 'SEPAL WIDTH'})
iris_df = iris_df.rename(columns={'petal_length': 'PETAL LENGTH'})
iris_df = iris_df.rename(columns={'petal_width': 'PETAL WIDTH'})
print(iris_df)
print('IL DataFrame <iris_df> è stato creato con successo!')
#print('Elimino le ultime tre colonne')
sepal_length = iris_df['SEPAL LENGTH']
sepal_width = iris_df['SEPAL WIDTH']
iris_df = iris_df.drop('PETAL LENGTH', axis = 1)
iris_df = iris_df.drop('PETAL WIDTH', axis = 1)
iris_df = iris_df.drop('species', axis = 1)
X = iris_df.to_numpy()

iris = datasets.load_iris()
y = iris.target
clf = svm.SVC()
clf.fit(X, y)

sl = askfloat('Entry', "Inserisci la lunghezza del sepalo")
sw = askfloat('Entry', "Inserisci la larghezza del sepalo")
p = clf.predict([[sl, sw]])
p = "{0}".format(p)
# let's convert <p> into a character string
if p == '[0]':
	print('La specie è <Iris setosa>')
elif p == '[1]':
	print('La specie è <Iris versicolor>')
elif p == '[2]':
	print('La specie è <Iris virginica>')
