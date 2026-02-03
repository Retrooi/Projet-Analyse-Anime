import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def setup_visualization():
    plt.style.use('default')
    sns.set_style("whitegrid")
    output_dir = Path("outputs/visualizations")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir

def plot_score_distribution(df, output_dir):
    plt.figure(figsize=(10,6))
    plt.hist(df['Score_Composite'], bins=20, color='purple', alpha=0.7)
    plt.title('Distribution Score Composite')
    plt.savefig(output_dir / 'score_distribution.png')
    print("Graphique sauvegarde : score_distribution.png")

def plot_regularity_impact(df, output_dir):
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Segment_Editorial', y='Regularite')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'impact_regularite.png')