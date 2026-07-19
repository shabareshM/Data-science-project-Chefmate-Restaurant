import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv("data/cleaned_restaurants.csv")

print("Dataset Shape:", df.shape)

# =====================================================
# Features for Clustering
# =====================================================

features = [
    "Average Cost for two",
    "Aggregate rating",
    "Votes",
    "Latitude",
    "Longitude",
    "Has Online delivery",
    "Has Table booking"
]

# Check if columns exist
missing = [col for col in features if col not in df.columns]

if missing:
    print("Missing Columns:", missing)
    exit()

X = df[features].copy()

# =====================================================
# Fill Missing Values
# =====================================================

X = X.fillna(X.median())

# =====================================================
# Feature Scaling
# =====================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =====================================================
# Find Best K using Silhouette Score
# =====================================================

best_score = -1
best_k = 2

scores = []

print("\nTesting K values...\n")

for k in range(2,11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)

    scores.append(score)

    print(f"K={k}   Score={score:.3f}")

    if score > best_score:
        best_score = score
        best_k = k

print("\nBest K :", best_k)

# =====================================================
# Train Final Model
# =====================================================

kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# =====================================================
# Save Model
# =====================================================

os.makedirs("models", exist_ok=True)

joblib.dump(kmeans, "models/kmeans_model.pkl")

joblib.dump(scaler, "models/scaler.pkl")

# =====================================================
# Save Clustered Dataset
# =====================================================

df.to_csv("data/clustered_restaurants.csv", index=False)

# =====================================================
# PCA Visualization
# =====================================================

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10,6))

plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=df["Cluster"],
    cmap="viridis"
)

plt.title("Restaurant Clusters")

plt.xlabel("PCA 1")

plt.ylabel("PCA 2")

plt.colorbar(label="Cluster")

plt.show()

# =====================================================
# Elbow Curve
# =====================================================

wcss=[]

for k in range(2,11):

    km = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    km.fit(X_scaled)

    wcss.append(km.inertia_)

plt.figure(figsize=(8,5))

plt.plot(range(2,11),wcss,marker="o")

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.grid()

plt.show()

print("\n===================================")
print("Training Completed Successfully")
print("===================================")

print("Best Cluster :",best_k)

print("Silhouette Score :",round(best_score,3))

print("\nFiles Saved")

print("models/kmeans_model.pkl")

print("models/scaler.pkl")

print("data/clustered_restaurants.csv")