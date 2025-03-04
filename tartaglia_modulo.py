from tkinter.simpledialog import askinteger
#n = askinteger('Entry', 'Inserisci il numero di termini da sommare')
n = 38
N = n + 3
print('Il programma restituisce la riga del Triangolo di Tartaglia formata da %d numeri' % N)

def tartaglia(n):
    sequenza_iniziale = [1,2,1]
    unità = 1
    for j in range(n):
        sequenza_nuova = [1]
        for i in range(len(sequenza_iniziale)-1):
            sequenza_nuova.append(sequenza_iniziale[i]+sequenza_iniziale[i+1])  
        sequenza_nuova.append(unità)
        sequenza_iniziale = sequenza_nuova
    return sequenza_nuova

sequenza_nuova = tartaglia(n)
