import pandas as pd
from sklearn.manifold import trustworthiness
import os

# Fichiers exportés
methods_files = {
    "PCA": "outputs/pca_2d.csv",
    "t-SNE": "outputs/tsne_result.csv",
    "UMAP": "outputs/umap_emb_2d.csv"
}

# Choisir les méthodes à comparer
methods_to_test = ["PCA", "t-SNE", "UMAP"]

# Vérifier que les fichiers existent
for method in methods_to_test:
    if method not in methods_files:
        raise ValueError(f"Méthode inconnue : {method}")
    if not os.path.exists(methods_files[method]):
        raise FileNotFoundError(f"Fichier {methods_files[method]} manquant.")
    
# Charger les données originales pour calcul de trustworthiness
X_original = pd.read_csv("data/city_lifestyle_dataset.csv").select_dtypes(include=['number'])

# Dictionnaire pour stocker les scores
scores = {}

# Calculer le score de trustworthiness
for method in methods_to_test:
    X_reduced = pd.read_csv(methods_files[method])
    # Ne conserver que les colonnes numériques (PC1, PC2)
    X_reduced_numeric = X_reduced.select_dtypes(include=['number'])
    scores[method] = trustworthiness(X_original, X_reduced_numeric, n_neighbors=10)

# Afficher les résultats
print("Trustworthiness scores :")
for method, score in scores.items():
    print(f"{method} : {score:.4f}")