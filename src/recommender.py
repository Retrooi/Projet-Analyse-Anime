import pandas as pd
from config import TOP_RECOMMENDATIONS_PATH

def save_top_recommendations(df):
    top = df[df['Segment_Editorial'].isin(['Chef-d_oeuvre', 'Excellente qualite'])]
    top = top.sort_values('Score_Composite', ascending=False).head(20)
    top.to_csv(TOP_RECOMMENDATIONS_PATH, index=False)
    return top

def display_recommendations(df, name):
    print(f"Recommandations pour {name} (Simulation basique)...")