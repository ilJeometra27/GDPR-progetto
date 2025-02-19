# GDPR-progetto
Generazione e Gestione Sicura di Dati Utente in Conformità al GDPR

Descrizione del Progetto

Questo progetto ha lo scopo di dimostrare la generazione, archiviazione e gestione sicura dei dati utente in conformità al GDPR.
Utilizza Python per generare dati casuali, salvarli in un file Excel e trasferirli in un database SQLite.

Python 3
Librerie Python:

random e string per la generazione di dati casuali
pandas per la manipolazione e archiviazione dei dati
sqlite3 per la gestione del database SQL
SQLite per l'archiviazione dei dati

Struttura del Progetto

Generazione dati utente.py: Script per la generazione di dati casuali e salvataggio in un file Excel.
README.md: Documentazione del progetto.
utenti_decreto.xlsx: File generato contenente i dati degli utenti.
utenti_decreto.db: Database SQLite con i dati importati.

Installazione e Utilizzo

Clonare la Repository

git clone https://github.com/ilJeometra/GDPR-progetto.git
cd GDPR-progetto

Installare le Dipendenze

Assicurarsi di avere Python installato, quindi eseguire:
pip install pandas openpyxl

Generare i Dati Utente

Eseguire lo script per creare il file Excel con i dati generati:
python Generazione_dati_utente.py
