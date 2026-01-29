import numpy as np

dati = np.random.randint(10,100, size= (6,5))
print('Dati originali : \n', dati)

print('\nShape: ', dati.shape)
print('Tipo di dato: ', dati.dtype)

print('\nPrima riga: ', dati[0])
print('Prima colonna: ',dati[:,0])
print('Sub - matrice (prime due righe e prime due colonne):\n', dati[:2,:3] )

view = dati[:2,:2]
copy = dati[:2,:2].copy

view[0,0] = 999

print('Dopo modifica della view:\n', dati)
print('La copy resta invariata\n', copy)

reshaped = dati.reshape(3,10)
print('\nArray reshaped ( 3 x 10): \n', reshaped)

print('\nIterazione su ogni elemento con nditer:')
for x in np.nditer(dati):
    print(int(x), end = ' ')
print()

extra = np.random.randint(10,100, size= (6,2))
unito = np.hstack((dati,extra))
print('\nArray unito con nuove colonne:\n ',unito)

split= np.split(unito,2)
print('\nArray diviso in due blocchi:\n',split[0],'\n',split[1])

mask = dati > 50
print('\nValori maggior di 50: \n', dati[mask])

ordinati = np.sort(dati, axis= 1)
print('\nDati ordinati su riga:\n', ordinati)

radici = np.sqrt(dati)
print('\nRadici quadrate di ogni elemento:\n',radici)