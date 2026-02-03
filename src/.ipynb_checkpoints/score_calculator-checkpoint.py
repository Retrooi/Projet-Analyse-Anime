import pandas as pd
from config import PONDERATION_GLOBALE, PONDERATION_MEILLEUR, PONDERATION_REGULARITE

def calculate_metrics(df):
    df_calc = df.copy()
    df_calc['Ecart_Qualite'] = df_calc['Note_Meilleur_Ep'] - df_calc['Note_Pire_Ep']
    df_calc['Regularite'] = (10 - df_calc['Ecart_Qualite']).clip(0, 10)
    return df_calc

def calculate_composite_score(df):
    df_score = df.copy()
    df_score['Score_Composite'] = (
        PONDERATION_GLOBALE * df_score['Note_Globale'] +
        PONDERATION_MEILLEUR * df_score['Note_Meilleur_Ep'] +
        PONDERATION_REGULARITE * df_score['Regularite']
    )
    # Normalisation sur 10 (optionnel)
    df_score['Score_Normalise'] = df_score['Score_Composite']
    return df_score

def display_score_stats(df):
    print(f"Score composite moyen : {df['Score_Composite'].mean():.2f}")