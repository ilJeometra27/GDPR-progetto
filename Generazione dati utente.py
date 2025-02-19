# Importazione delle librerie necessarie
import random
import string
import pandas as pd
import sqlite3

# Funzione per generare dati casuali per gli utenti
# Ogni utente avrà un nome, un cognome, un'email e un numero di telefono.
def generate_random_user():
    first_name = ''.join(random.choices(string.ascii_letters, k=8)).capitalize()
    last_name = ''.join(random.choices(string.ascii_letters, k=10)).capitalize()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    phone = f"+39 {random.randint(300, 399)}-{random.randint(1000000, 9999999)}"
    return {
        "Nome": first_name,
        "Cognome": last_name,
        "Email": email,
        "Telefono": phone
    }

# Generazione di dati per 10 utenti
# Viene creato un elenco di 10 dizionari, ciascuno rappresentante un utente con dati casuali.
user_data = [generate_random_user() for _ in range(10)]

# Creazione di un DataFrame pandas per gestire i dati
# Il DataFrame è utile per organizzare e manipolare i dati in modo strutturato.
user_df = pd.DataFrame(user_data)

# Esportazione dei dati in un file Foglio di calcolo elettronico
# Il file Foglio di calcolo elettronico viene salvato nella directory corrente con il nome 'utenti_gdpr.xlsx'.
FoglioDiCalcoloElettronico_file = "utenti_gdpr.xlsx"
user_df.to_excel(FoglioDiCalcoloElettronico_file, index=False)
print(f"File Excel'{FoglioDiCalcoloElettronico_file}' generato con successo.")

# Creazione di un database SQLite
# La connessione al database SQLite consente di creare e gestire una tabella per i dati degli utenti.
conn = sqlite3.connect("utenti_gdpr.db")
cursor = conn.cursor()

# Creazione della tabella SQL
# La tabella 'utenti' contiene quattro colonne: Nome, Cognome, Email e Telefono.
cursor.execute('''
CREATE TABLE IF NOT EXISTS utenti (
    Nome TEXT,
    Cognome TEXT,
    Email TEXT,
    Telefono TEXT
)
''')

# Inserimento dei dati dal DataFrame nella tabella SQL
# Ogni riga del DataFrame viene inserita come record nella tabella SQL.
for _, row in user_df.iterrows():
    cursor.execute('''
    INSERT INTO utenti (Nome, Cognome, Email, Telefono) 
    VALUES (?, ?, ?, ?)
    ''', (row['Nome'], row['Cognome'], row['Email'], row['Telefono']))

# Salvataggio e chiusura della connessione al database
conn.commit()
conn.close()
print("Tabella SQL popolata con successo dai dati del file Foglio di calcolo elettronico.")
