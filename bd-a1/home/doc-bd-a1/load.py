import sys
import pandas as pd
import subprocess

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)

        temp_path = '/home/doc-bd-a1/temp_data.csv'
        df.to_csv(temp_path, index=False)

        subprocess.run(['python3', 'dpre.py', temp_path])

    except Exception as e:
        print(f"Error loading: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <dataset-path>")
        sys.exit(1)

    file_path = sys.argv[1]
    load_data(file_path)
