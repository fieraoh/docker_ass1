import sys
import pandas as pd
import subprocess

def perform_eda(file_path):
    df = pd.read_csv(file_path)

    # Insight 1: Basic Statistics
    insight1 = df.describe().to_string()
    with open('/home/doc-bd-a1/eda-in-1.txt', 'w') as f:
        f.write("Basic Statistical Analysis:\n" + insight1)

    # Insight 2: Missing Values
    insight2 = f"Missing Values Analysis:\n{df.isnull().sum().to_string()}"
    with open('/home/doc-bd-a1/eda-in-2.txt', 'w') as f:
        f.write(insight2)

    # Insight 3: Data Distribution
    insight3 = "Data Distribution Analysis:\n"
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        insight3 += f"\n{column}:\n"
        insight3 += f"Skewness: {df[column].skew()}\n"
        insight3 += f"Kurtosis: {df[column].kurtosis()}\n"

    with open('/home/doc-bd-a1/eda-in-3.txt', 'w') as f:
        f.write(insight3)

    # Call next script...
    subprocess.run(['python3', 'vis.py', file_path])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <dataset-path>")
        sys.exit(1)

    file_path = sys.argv[1]
    perform_eda(file_path)