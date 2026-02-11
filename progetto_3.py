import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Dati cliente di esempio
nome ='Giovanni Mazzotta' 
eta = 27
saldo_conto = 3000.00 
vip = True

#Lista destinazioni e dizionario prezzi
destinazioni =  ['Parigi', 'Tokyo', 'Dubai', 'Madrid', 'New york']
prezzi = {destinazioni[0] : 1000, destinazioni[1] : 1200, destinazioni[2] : 800, destinazioni[3] : 900, destinazioni[4] : 1100}

#Definizioni delle classi e funzzioni
class Cliente:
    def __init__(self,nome,eta,vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def Presentazione(self):
        return f'Nome cliente {self.nome} - Età: {self.eta} - Stato cliente VIP: {self.vip}'
    
class Viaggio:
    def __init__(self, destinazione, prezzo, durata_giorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata_giorni = durata_giorni

class Prenotazione:
    def __init__(self,cliente,viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    def clalcola_importo_finale(self):
        prezzo = self.viaggio.prezzo
        if self.cliente.vip:
            prezzo = prezzo * 0.9
        return prezzo
    
    def dettagli(self):

        importo_finale = self.clalcola_importo_finale()
        return f'Cliente: {self.cliente.nome} - Destinazione: {self.viaggio.destinazione} - Durata: {self.viaggio.durata_giorni} - Importo: {importo_finale:.2f} $'


#Simulazione e statistiche sui prezzi

np.random.seed(42) #seed per dati casuali

prezzo_prenotazioni = np.random.randint(200,2001,100)
media_prezzo = np.mean(prezzo_prenotazioni)
prezzo_min = np.min(prezzo_prenotazioni)
prezzo_max = np.max(prezzo_prenotazioni)
dev_std = np.std(prezzo_prenotazioni)

#Percentuali prezzi sopra la media
sopra_media = prezzo_prenotazioni > media_prezzo
percentuale_sopra_media = np.sum(sopra_media) / len(prezzo_prenotazioni) * 100

#Stampa dei risultati
print(f'Prezzo medio: {media_prezzo:.2f} $')
print(f'Prezzo minimo: {prezzo_min} $')
print(f'Prezzo massimo: {prezzo_max} $')
print(f'Deviazione standard: {dev_std:.2f} $')
print(f'Percentuale sopra la media: {percentuale_sopra_media:.2f} % ')

#Creazione DataFrame simulato
clienti = ['Giovanni', 'Marco', 'Paolo', 'Giulia', 'Erika', 'Sara']

dati =  {
    'Cliente' : np.random.choice(clienti,100),
    'Destinazione' : np.random.choice(destinazioni,100),
    'Prezzo' : np.random.randint(200,2001,100),
    'Giorno_partenza' : pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(0,180,100), unit='D'),
    'Durata' : np.random.randint(3,15,100)
    }

df = pd.DataFrame(dati)

#Incasso

df['Incasso'] = df['Prezzo'] * df['Durata']

#Incasso totale
incasso_totale = np.sum(df['Incasso'])
print(incasso_totale)

#Incasso per desinazione
incasso_per_destinazione = df.groupby('Destinazione')['Incasso'].sum()
print(incasso_per_destinazione)

#Incasso medio per destinazione
incasso_medio_per_dest = df.groupby('Destinazione')['Incasso'].mean()
print(incasso_medio_per_dest.round(2))

#Top 3 destianzioni
conteggio_destinazioni = df['Destinazione'].value_counts()
top3_dest = conteggio_destinazioni.head(3)
print(top3_dest)

#Grafico a barre: incasso medio per destinazione
plt.figure(figsize=(7,5))
incasso_medio_per_dest.plot(kind='bar', color='blue', edgecolor= 'black')
plt.title('Incasso totale per destinazione')
plt.xlabel('Destinazione')
plt.ylabel('Incasso ($)')
plt.grid(linestyle='--', alpha= 0.6)
plt.show()

#Grafico a linee: andamento giornaliero incasso
incasso_giornaliero = df.groupby('Giorno_partenza')['Incasso'].sum().sort_index()
plt.figure(figsize=(10,5))
incasso_giornaliero.plot(kind='line', marker='o', color='green', linestyle='-')
plt.title('Andamento giornaliero incassi')
plt.xlabel('Giorno di partenza')
plt.ylabel('Incasso ($)')
plt.grid(True, linestyle='--', alpha = 0.6)
plt.show()

#Grafico a torta: percentuale prenotazioni per destinazione
plt.figure(figsize=(7,5))
conteggio_destinazioni.plot(kind='pie', labels=conteggio_destinazioni.index, autopct= '%1.1f%%',colors=['red','blue','green','yellow','skyblue'])
plt.title('Percentuale di prenotazioni per destinazione')
plt.show()

#Aggiunta colonna continente
destinazione_continente = {'Parigi' : 'Europa', 'Madrid' : 'Europa', 'Tokyo' : 'Asia', 'Dubai' : 'Africa', 'New york' : 'America'}
df['Continente'] = df['Destinazione'].map(destinazione_continente)

#Incasso e durata media per continente
incasso_per_continente = df.groupby('Continente')['Incasso'].sum()
durata_media_continente = df.groupby('Continente')['Durata'].mean()

#Salvataggio DataFrame in csv
df.to_csv(' prenotazioni_analizzate.csv')

#Funzione top 3 clienti
def top_clienti(df,N=5):
        return df['Cliente'].value_counts().head(N)
print(top_clienti(df, 3))

#Grafico combinato: barre = incasso medio, linea = durata media per continente
gruppo_categoria = df.groupby('Continente').agg({'Incasso' : 'mean', 'Durata' : 'mean'}).sort_index()

fig,ax1 = plt.subplots(figsize=(8,5))

#grafico a barre
ax1.bar(gruppo_categoria.index, gruppo_categoria['Incasso'], color='blue', edgecolor= 'black', label='Incasso medio')
ax1.set_ylabel('Incasso medio ($)')

#Grafico linee
ax2 = ax1.twinx() #secondo asse y
ax2.plot(gruppo_categoria.index, gruppo_categoria['Durata'], color= 'red', marker='o', linewidth= 2, label='Durata media')
ax2.set_ylabel('Durata media (giorni)')

fig.suptitle("Incasso medio e durata media per categoria")

plt.show()
