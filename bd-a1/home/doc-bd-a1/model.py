import sys
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def apply_kmeans(file_path):
    df = pd.read_csv(file_path)

    # Select columns for clustering (nummrical)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    X = df[numeric_cols]

    # Apply K means
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X)

    # Count records in each cluster
    cluster_counts = np.bincount(clusters)

    # Save cluster counts
    with open('/home/doc-bd-a1/k.txt', 'w') as f:
        for i, count in enumerate(cluster_counts):
            f.write(f"Cluster {i}: {count} records\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model.py <dataset-path>")
        sys.exit(1)

    file_path = sys.argv[1]
    apply_kmeans(file_path)
