# svm2.py

import os
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
# os.system('sudo apt-get install python3-sklearn python3-sklearn-lib python-sklearn-doc')
import pandas as pd
from sklearn import svm, datasets
#os.system('mkdir COMPUTER_SCIENCE')
#os.chdir('/home/%s/COMPUTER_SCIENCE' % user)
#os.system('mkdir AI')
#os.chdir('AI')

os.system('wget wget https://raw.githubusercontent.com/pierorivoira/COMPUTER-SCIENCE/refs/heads/main/iris.csv')
print('Ho scaricato il file <iris.csv> da https://github.com/pierorivoira/COMPUTER-SCIENCE')
iris_df = pd.read_csv('iris.csv')
print(iris_df)
print('IL DataFrame <iris_df> è stato creato con successo!')
