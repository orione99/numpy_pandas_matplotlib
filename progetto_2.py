import numpy as np

class Paziente:
    def __init__(self,nome, cognome, codice_fiscale, eta, peso, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.risultati_analisi = np.array(risultati_analisi)
        self.analisi = []

    def aggiungi_analisi(self,analisi):
        self.analisi.append(analisi)
    
    def scheda_personale(self):
        return f'\nScheda personale:\nNome: {self.nome}\nCognome: {self.cognome}\nCodice fiscale: {self.codice_fiscale}\nEtà: {self.eta}\nPeso: {self.peso}\nAnalisi effettuate: {self.risultati_analisi}'

    def statistiche_analisi(self):
        media = np.mean(self.risultati_analisi)
        minimo = np.min(self.risultati_analisi)
        massimo = np.max(self.risultati_analisi)
        deviazione_std = np.std(self.risultati_analisi)

        return {
            "media": float(round(media,2)),
            "minimo": float(round(minimo,2)),
            "massimo": float(round(massimo,2)),
            "deviazione_standard": float(round(deviazione_std,2))
        }


class Medico():
    def __init__(self,nome,cognome,specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzaione = specializzazione

    def visita_paziente(self,paziente):
        print(f'Il medico: {self.nome} {self.cognome}\n spiecializzato in {self.specializzaione}\n sta visitando il paziente {paziente.nome} {paziente.cognome}')

class Analisi:
    valori_normali = {
        "glicemia": (70, 100),
        "colesterolo": (0, 200),
        "trigliceridi": (0, 150)
    }

    def __init__ (self, tipo, risultato):
        self.tipo = tipo
        self.risultato = risultato

    def valuta(self):
        if self.tipo not in self.valori_normali:
            return 'Valutazione non disponibile'
        
        minimo,massimo = self.valori_normali[self.tipo]
        if minimo <= self.risultato <= massimo:
            return 'Risultati nella norma'
        else:
            return 'Risultati non nella norma'
        
risultati_glicemia = np.array([100, 130, 97, 92, 110, 150, 122, 87, 65, 101])
print('\nRisultati glicemia: ')
media = np.mean(risultati_glicemia)
valore_massimo = np.max(risultati_glicemia)
valore_minimo = np.min(risultati_glicemia)
deviazione_std= np.std(risultati_glicemia)

print("Media:", media)
print("Valore massimo:", valore_massimo)
print("Valore minimo:", valore_minimo)
print("Deviazione standard:", deviazione_std)
     
if __name__ == "__main__":
    # Creazione medici
    medici = [
        Medico("Luca", "Rossi", "Cardiologo"),
        Medico("Maria", "Bianchi", "Endocrinologo"),
        Medico("Paolo", "Verdi", "Medico Generico")
    ]

    # Creazione pazienti
    pazienti = [
        Paziente("Giovanni", "Neri", "GNVN01", 25, 70, [92, 185, 120]),
        Paziente("Erika", "Ferri", "ERKF02", 24, 60, [88, 170, 110]),
        Paziente("Lorenzo", "Russo", "LORR03", 30, 80, [105, 200, 140]),
        Paziente("Sara", "Galli", "SARG04", 28, 65, [95, 180, 130]),
        Paziente("Marco", "Landi", "MARL05", 35, 75, [100, 190, 150])
    ]

    tipi_analisi = ["glicemia", "colesterolo", "trigliceridi"]

    # Aggiunta Analisi 
    for paz in pazienti:
        for i in range(len(tipi_analisi)):
            paz.aggiungi_analisi(Analisi(tipi_analisi[i], paz.risultati_analisi[i]))

    # Stampa schede personali
    for paz in pazienti:
        print("------ Scheda Paziente ------")
        print(paz.scheda_personale())

    # Medici che visitano i pazienti
    print("\n------ Visite Mediche ------")
    for i, paziente in enumerate(pazienti):
        medico = medici[i % len(medici)]  # cicla tra i medici
        medico.visita_paziente(paziente)

    # Statistiche analisi
    print("\n------ Statistiche Analisi ------")
    for paz in pazienti:
        stats = paz.statistiche_analisi()
        print(f"{paz.nome} {paz.cognome}: {stats}")

