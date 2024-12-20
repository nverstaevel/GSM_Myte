import requests
import pandas as pd
from datetime import datetime

# URL et paramètres pour la requête
url = "https://couverture-mobile.orange.fr/arcgis/rest/services/extern/siteshs/MapServer/0/query"
params = {
    'f': 'json',
    'where': "perimetre='MAY'",
    'outFields': '*'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Envoyer la requête GET
response = requests.get(url, params=params, headers=headers)

# Vérifier le statut de la réponse
if response.status_code == 200:
    data = response.json()

    # Extraire les features
    features = data['features']
    attributes_list = [feature['attributes'] for feature in features]

    # Convertir les données en DataFrame
    df = pd.DataFrame(attributes_list)

    # Obtenir la date et l'heure actuelle et formater le nom du fichier
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'data_{current_datetime}.xlsx'

    # Exporter les données vers une feuille Excel
    df.to_excel(filename, index=False)
    print(f"Données exportées vers {filename} avec succès.")
else:
    print(f"Error: {response.status_code}")
