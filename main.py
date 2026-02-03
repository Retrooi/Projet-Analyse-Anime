import sys
# Ajout du dossier src au chemin pour les imports
sys.path.append('src')

from data_loader import load_data, display_info
from data_cleaner import clean_data, check_missing_values
from score_calculator import calculate_metrics, calculate_composite_score, display_score_stats
from segmenter import segment_animes, display_segment_stats
from visualizer import setup_visualization, plot_score_distribution, plot_regularity_impact
from recommender import save_top_recommendations, display_recommendations
from report_generator import generate_statistical_report, generate_top_recommendations_table
from config import CLEANED_DATA_PATH, ENRICHED_DATA_PATH

def main():
    print("=== PROJET ANALYSE ANIMES ===")
    
    # 1. Chargement
    try:
        df = load_data()
    except FileNotFoundError:
        print("ERREUR: Placez le fichier 'animes.csv' dans le dossier 'data' !")
        return

    display_info(df)
    
    # 2. Nettoyage & Calculs
    df_clean = clean_data(df)
    df_metrics = calculate_metrics(df_clean)
    df_scored = calculate_composite_score(df_metrics)
    
    # 3. Segmentation
    df_segmented = segment_animes(df_scored)
    display_segment_stats(df_segmented)
    
    # 4. Outputs
    out_dir = setup_visualization()
    plot_score_distribution(df_segmented, out_dir)
    plot_regularity_impact(df_segmented, out_dir)
    
    save_top_recommendations(df_segmented)
    generate_statistical_report(df_segmented)
    
    # 5. Save Data
    df_segmented.to_csv(ENRICHED_DATA_PATH, index=False)
    print("\n=== SUCCES : Tout est termine ! ===")

if __name__ == "__main__":
    main()