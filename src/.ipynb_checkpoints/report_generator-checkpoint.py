from datetime import datetime
def generate_statistical_report(df, path="outputs/reports/rapport.txt"):
    with open(path, 'w') as f:
        f.write(f"Rapport genere le {datetime.now()}\n")
        f.write(f"Nombre animes : {len(df)}")
    print("Rapport genere.")

def generate_top_recommendations_table(df):
    print(df[['Anime', 'Score_Composite', 'Segment_Editorial']].head(10))