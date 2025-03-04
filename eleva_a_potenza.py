import math
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askinteger
n = askinteger('Entry', 'Inserisci il numero di termini da sommare (es. 100)')
z = askfloat('Entry', "Inserisci l'esponente")
print('La somma sarà effettuata su %d termini' % n)
print('La base dei logaritmi naturali %f sarà elevata alla %f-esima potenza' % (math.e, z))

def eleva_a_potenza(n,z):
    somma = []
    for i in range(n):
            result = z**i / math.factorial(i)
            somma.append(result)
            output = sum(somma)
    return output

output = eleva_a_potenza(n,z)
print('Il risultato è %f' % output)
