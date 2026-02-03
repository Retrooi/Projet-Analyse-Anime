import pandas as pd
import numpy as np

def clean_data(df):
    df_clean = df.copy()
    df_clean = df_clean.drop_duplicates()
    df_clean['Note_Pire_Ep'] = df_clean['Note_Pire_Ep'].fillna(0)
    df_clean['Pire_Ep_Titre'] = df_clean['Pire_Ep_Titre'].fillna('Non specifie')
    df_clean['Nb_Episodes'] = pd.to_numeric(df_clean['Nb_Episodes'], errors='coerce').fillna(12)
    return df_clean

def check_missing_values(df):
    missing = df.isnull().sum()
    total = missing.sum()
    print(f"Total valeurs manquantes : {total}")
    return missing