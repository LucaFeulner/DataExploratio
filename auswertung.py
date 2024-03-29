import pandas as pd
import numpy as mp
import matplotlib.pyplot as pyplot
import seabron as sns

data = pd.read_csv("Daten/data.csv")

print(data.head())
print(data.info())



# Initialisiere den Geocoder
geolocator = Nominatim(user_agent="Test")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, error_wait_seconds=10)

# Überprüfe, ob die test.csv Datei existiert und lade sie gegebenenfalls
existing_entries = {}
if os.path.exists('Daten/test.csv'):
    existing_df = pd.read_csv('Daten/test.csv')
    # Erstelle ein Dictionary der existierenden Einträge für schnellen Zugriff
    existing_entries = {row['Adress']: (row['Latitude'], row['Longitude']) for index, row in existing_df.iterrows() if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude'])}
else:
    print("Keine existierende 'test.csv' gefunden.")

# Funktion zum Speichern einer Zeile in die CSV-Datei
def save_row_to_csv(row, file_path, mode='a'):
    row.to_csv(file_path, mode=mode, header=not os.path.exists(file_path), index=False)

# Start der Verarbeitung und sofortiges Speichern
for index, row in df.iterrows():
    address = row['Adress']
    if address not in existing_entries:
        try:
            # Führe Geokodierung durch
            location = geocode(address)
            if location:
                latitude, longitude = location.latitude, location.longitude
                print(f"Umwandlung erfolgreich: {address} -> {latitude}, {longitude}")
                # Speichere die aktuelle Zeile direkt in die CSV-Datei
                save_row_to_csv(pd.DataFrame([[address, latitude, longitude]], columns=['Adress', 'Latitude', 'Longitude']), 'Daten/test.csv')
            else:
                print(f"Kein Ergebnis für: {address}")
        except Exception as e:
            print(f"Fehler bei der Geokodierung für: {address} - {e}")
        # Sicherstellen, dass wir die API-Beschränkungen einhalten
        time.sleep(1)
    else:
        print(f"Eintrag bereits vorhanden: {address}")

print("Die Datei wurde erfolgreich mit allen Zeilen erstellt und aktualisiert.")