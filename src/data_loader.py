import pandas as pd
from pathlib import Path
from config import DATA_PATH

def load_data(file_path=DATA_PATH):
    if not Path(file_path).exists():
        # Fallback si lancé depuis la racine
        if Path(f"../{file_path}").exists():
            file_path = f"../{file_path}"
        else:
            raise FileNotFoundError(f"Fichier non trouve : {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"Donnees chargees : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return df

def display_info(df):
    print("="*50)
    print("INFORMATIONS SUR LES DONNEES")
    print("="*50)
    print(f"Dimensions : {df.shape[0]} animes, {df.shape[1]} colonnes")
    if 'Note_Globale' in df.columns:
        print(f"Moyenne Note Globale : {df['Note_Globale'].mean():.2f}/10")