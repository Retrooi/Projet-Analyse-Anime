import pandas as pd
from config import SEUIL_CHEF_DOEUVRE, SEUIL_EXCELLENT, SEUIL_POTENTIEL, SEUIL_ECART_RISQUE, SEUIL_A_EVITER

def segment_animes(df):
    df_seg = df.copy()
    def categorize(row):
        if row['Score_Composite'] >= SEUIL_CHEF_DOEUVRE and row['Regularite'] >= 7:
            return 'Chef-d_oeuvre'
        elif row['Score_Composite'] >= SEUIL_EXCELLENT and row['Regularite'] >= 6:
            return 'Excellente qualite'
        elif row['Score_Composite'] >= SEUIL_POTENTIEL and row['Note_Meilleur_Ep'] >= 9.0:
            return 'Potentiel eleve'
        elif row['Ecart_Qualite'] >= SEUIL_ECART_RISQUE:
            return 'Variable (risque)'
        elif row['Score_Composite'] < SEUIL_A_EVITER:
            return 'A eviter'
        else:
            return 'Standard'
    df_seg['Segment_Editorial'] = df_seg.apply(categorize, axis=1)
    return df_seg

def display_segment_stats(df):
    print(df['Segment_Editorial'].value_counts())