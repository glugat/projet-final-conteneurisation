import pandas as pd
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler  # t-SNE aime les données normalisées

# Charge les données
df = pd.read_csv("data/votre_fichier.csv")  # adapte le chemin/nom
X = df.drop(columns=["label"])              # features sans label (adapte)
y = df["label"]                             # colonne label (adapte ou supprime si pas de labels)

# Normalise
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applique t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000)  # perplexity=30 souvent optimal
X_tsne = tsne.fit_transform(X_scaled)

# Sauvegarde résultat
result = pd.DataFrame(X_tsne, columns=["tSNE1", "tSNE2"])
result["label"] = y
result.to_csv("outputs/tsne_result.csv", index=False)

print(f"KL divergence: {tsne.kl_divergence_}")  # métrique de qualité (plus bas = mieux)

