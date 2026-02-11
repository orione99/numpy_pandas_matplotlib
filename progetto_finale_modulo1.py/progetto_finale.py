import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leggo il file .csv che abbiamo in cartella, stampo prime 5 righe, numero di righe e colonne e le sue informazioni generali
df = pd.read_csv('vendite.csv')
print(f'Prime 5 righe del file: \n{df.head(5)}\nNumero di righe e colonne: {df.shape}')
print(df.info())

# Definisco una nuova colonna 'incasso'
df['incasso'] = df['quantita'] * df['prezzo_unitario']

# Definisco incasso totale, incasso medio per negozio, prodotto piu venduti in ordine decrescente e incasso medio di prodotto per negozio.
incasso_totale = df['incasso'].sum()
incasso_medio_x_negozio = df.groupby('negozio')['incasso'].mean()
pro_piu_vend = df.groupby('prodotto')['quantita'].sum().sort_values(ascending=False)
incasso_m_neg_pro = df.groupby(['negozio','prodotto'])['incasso'].mean()

# Stampo i risultati
print(
    f'Incasso totale: {incasso_totale.round(2)}\nIncasso medio per negozio: {incasso_medio_x_negozio}\n' 
    f'Prodotto piu venduto: {pro_piu_vend}\nIncasso medio di ogni prodotto per negozio: {incasso_m_neg_pro}'
      )

# estraggo colonna quantita come array e calcolo: media, minimo, max, deviazione standard e percentuale di vendita sopra la media 
q = df['quantita'].to_numpy()
media = np.mean(q)
minimo = np.min(q)
massimo = np.max(q)
dev_std = np.std(q)
sopra_media = q > media
percentuale_sopra_media = np.sum(sopra_media) / len(q) * 100

# stampo i risultati
print(
    f'Media: {media}\nMinimo: {minimo}\nMassimo: {massimo}\nDeviazione standard: {dev_std.round(2)}\n'
    f'Percentuale sopra la media: {percentuale_sopra_media.round(2)}'
    )

# Creo un array 2D con quantita e prezzo unitario e calcolo per ogni riga l'incasso
q_pu = df[['quantita','prezzo_unitario']].to_numpy().round(2)
incassi = q_pu[:,0] * q_pu[:,1]

# Stampo gli incassi
print(incassi)

# Confrontiamo tutto l'array con la colonna incasso del dataframe e stampiamo
confronto = incassi == df['incasso'].to_numpy()
print(f' Tutte le righe coincidono?', np.all(confronto))

## Grafico a barre del totale degli incassi per negozio 
# Ricaviamo prima gli incassi per negozio

incasso_tot_x_neg = df.groupby('negozio')['incasso'].sum()
print(incasso_tot_x_neg)

# Grafico a barre con relative dimensioni e specifiche
plt.figure(figsize=(10,8))
incasso_tot_x_neg.plot(kind='bar',color ='red',edgecolor = 'skyblue')
plt.title('Incasso totale per negozio')
plt.xlabel('NEGOZI')
plt.ylabel('INCASSI')
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.show()

## Grafico a torta della percentuale di incasso per prodotto 
# Ricaviamo gli incassi per prodotto

incasso_x_prodotto = df.groupby('prodotto')['incasso'].sum()
print(incasso_x_prodotto)

# Grafico a torta con relative dimensioni e specifiche
plt.figure(figsize = (10,8))
incasso_x_prodotto.plot(kind= 'pie', autopct = '%1.1f%%', colors = ['skyblue', 'red', 'yellow', 'blue', 'green','purple'])
plt.title('Percentuale incasso per prodotto')
plt.show()

## Grafico a linee con incasso giornaliero 
# ricaviamo l'incasso giornaliero

df['data'] = pd.to_datetime(df['data'])
incasso_giornaliero = df.groupby('data')['incasso'].sum().sort_index()
print(incasso_giornaliero)

# Grafico a linee con relative dimensioni e specifiche
plt.figure(figsize=(12,5))
incasso_giornaliero.plot(kind= 'line', marker = 'o', color = 'red', linestyle = '--')
plt.title('Incasso giornaliero')
plt.xlabel('DATA')
plt.ylabel('INCASSO')
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.show()

# Creo una categoria per ogni prodotto e l'aggiungo come colonna
categoria = {'Monitor': 'Schermi',
    'TV': 'Schermi',
    'Smartphone': 'Telefonia',
    'Tablet': 'Telefonia',
    'Cuffie': 'Auricolari',
    'Laptop': 'PC'}

df['categoria'] = df['prodotto'].map(categoria)

# Per ogni categoria calcolo incasso totale e quantità media venduta
incasso_tot_x_cat = df.groupby('categoria')['incasso'].sum()
q_media_vend_x_cat = df.groupby('categoria')['quantita'].mean()

# Stampo i risultati
print(f'Incasso totale per categoria: {incasso_tot_x_cat}\nQuantita media venduta per categoria: {q_media_vend_x_cat.round(2)}')

# Salvo il df in un nuovo file .csv
df.to_csv('vendite_analizzate.csv')

## Creo un grafico combinato (barre + linee) con incasso medio per categoria e quantita media venduta
# calcolo l'incasso medio per categoria 
incasso_m_x_cat = df.groupby('categoria')['incasso'].mean()

fig,ax1 = plt.subplots(figsize = (7,5))

# Grafico a barre
ax1.bar(incasso_m_x_cat.index, incasso_m_x_cat.values, color = 'red', edgecolor = 'black', label = 'Incasso medio per categoria')
ax1.set_ylabel('Incasso medio ($)')

#Grafico a linee
ax2 = ax1.twinx()
ax2.plot(q_media_vend_x_cat, color= 'black', marker='o', linewidth= 2, label= 'Quantita media')
ax2.set_ylabel('Quantità media venduta')

fig.suptitle('Incasso medio per categoria (barre) e quantita media venduta (linee)')

plt.show()

# Definisco una funzione che restituisca i prodotti piu venduti per incasso totale
def top_n_prodotti():
    return incasso_x_prodotto.sort_values(ascending=False)

# Testo la funzione
print(top_n_prodotti())