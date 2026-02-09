import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

date = pd.date_range('2023-01-01', periods=10, freq= 'ME')

vendite = [10, 20, 12, 15, 25, 22, 24, 28, 30, 35]

np.random.seed(42)
eta_clienti = np.random.randint(18, 65, 50)

spesa_media = eta_clienti * 2 + np.random.randint(-20, 20, 50)

plt.figure(figsize = (8,5))
plt.plot(date, vendite, marker = 'o', color= 'blue', linewidth= 2, linestyle= '--', label = 'vendite')
plt.title('Andamento mensile vendite 2023')
plt.xlabel('Mese')
plt.ylabel('Vendite (migliaia $)')
plt.legend()
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.show()

plt.figure(figsize= (7,5))
plt.hist(eta_clienti, bins = 8, color = 'skyblue', edgecolor= 'black', alpha = 0.8)
plt.title('Distribuzione età dei clienti')
plt.xlabel('Età')
plt.ylabel('Frrequenza')
plt.show()


plt.figure(figsize= (7,5))
plt.scatter(eta_clienti, spesa_media, color='red', marker = 'o', alpha= 0.7)
plt.title('Relazione tra età e spesa')
plt.xlabel('Età dei clienti')
plt.ylabel('Spesa medias in dollari ($)')
plt.grid(True, alpha= 0.6)
plt.show()

fig,ax= plt.subplots(2,2, figsize=(10,8))

ax[0,0].plot(date,vendite, marker='o', color= 'blue')
ax[0,0].set_title('Vendite mensili')

ax[0,1].hist(eta_clienti,bins = 8, color= 'orange', edgecolor= 'black')
ax[0,1].set_title('Distribuzione età')

ax[1,0].scatter(eta_clienti, spesa_media, color='green', alpha = 0.7)
ax[1,0].set_title('Età vs spesa')

ax[1,1].fill_between(date, vendite, color= 'lightblue', alpha = 0.6)
ax[1,1].plot(date, vendite, color= 'blue')
ax[1,1].set_title('Vendite comulative')

plt.tight_layout()
plt.show()