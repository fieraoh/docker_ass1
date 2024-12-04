import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

def create_visualization(file_path):
    df = pd.read_csv(file_path)

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation heatmap')
    plt.tight_layout()

    # Save to file
    plt.savefig('/home/doc-bd-a1/vis.png')
    plt.close()

    # Call next script...
    subprocess.run(['python3', 'model.py', file_path])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <dataset-path>")
        sys.exit(1)

    file_path = sys.argv[1]
    create_visualization(file_path)