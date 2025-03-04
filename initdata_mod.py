# initialize data to be stored in files, pickles, shelves

import os

user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)

# records
species_1 = {'NAME': 'Tachyglossus aculeatus', 'ORDER': 'Monotremata', 'METABOLIC RATE (Watt)': 2.404, 'BODY MASS': 2725, 'BODY TEMPERATURE': 30.7, 'AMBIENT TEMPERATURE': 19.7}
species_2 = {'NAME': 'Plecotus auritus', 'ORDER': 'Chiroptera', 'METABOLIC RATE (Watt)': 0.082, 'BODY MASS': 10.25, 'BODY TEMPERATURE': 35.5, 'AMBIENT TEMPERATURE': 4.4}

# database
db = {}
db['species_1'] = species_1
db['species_2'] = species_2

# if __name__ == '__main__':
for key in db:
	print(key, '=>\n   ', db[key])

