import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# On cherche le fichier
if os.path.exists('data/animes.csv'):
    path = 'data/animes.csv'
else:
    path = 'animes.csv'

# Chargement et Calculs
df = pd.read_csv(path)
df['Ecart'] = df['Note_Meilleur_Ep'] - df['Note_Pire_Ep'].fillna(0)
df['Regularite'] = (10 - df['Ecart']).clip(0, 10)
df['Score_Final'] = 0.4*df['Note_Globale'] + 0.3*df['Regularite'] + 0.3*df['Note_Meilleur_Ep']

# Résultats
print("TOP 5 ANIMÉS :")
print(df.sort_values('Score_Final', ascending=False).head(5)[['Anime', 'Score_Final']])

# Sauvegarde du graphique
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Note_Globale', y='Ecart', hue='Regularite')
plt.title("Analyse Finale")
plt.savefig('mon_graphique.png')
print("\n✅ Graphique 'mon_graphique.png' sauvegardé !")