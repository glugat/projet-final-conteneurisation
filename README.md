# MLSD M1 - Technologies de conteneurisation (projet)


## 1. Objectif
Ce projet simule un travail collaboratif de data science sur GitHub. L'objectif est de comparer plusieurs méthodes de réduction de dimension (PCA, t-SNE, UMAP) sur un jeu de données urbaines, puis d'évaluer la qualité de la réduction à l'aide de la métrique **trustworthiness**.

---

## 2. Structure du projet

├─ data/ # Données
├─ notebooks/ # Notebooks des méthodes (PCA, t-SNE, UMAP)
├─ outputs/ # Données projetées 2D exportées
├─ compare_methods.py # Script de comparaison des méthodes
├─ Dockerfile # Image Docker pour l'exécution du projet
└─ README.md

data/
├─ city_lifestyle_dataset.csv
notebooks/
├─ pca.ipynb
├─ tsne.ipynb
├─ umap.ipynb
outputs/
├─ pca_2d.csv
├─ tsne_2d.csv
├─ umap_2d.csv
compare_methods.py
Dockerfile
README.md

---

## 3. Méthodes de réduction de dimension

Chaque étudiant a développé une méthode dans une branche dédiée :
- PCA : Analyse en composantes principales
- t-SNE : T-distributed Stochastic Neighbor Embedding
- UMAP : Uniform Manifold Approximation and Projection

Chaque notebook :
- projette les données en 2D
- visualise les résultats par continent
- exporte les données 2D dans "outputs/"

---

## 4. Comparaison des méthodes

Le script "evaluate.ipynb" :
- charge les fichiers 2D exportés
- calcule la métrique **trustworthiness** pour chaque méthode
- affiche les scores pour comparer la préservation des voisinages locaux
