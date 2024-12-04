import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import subprocess

def preprocess_data(file_path):
    # Read the dataset
    df = pd.read_csv(file_path)

    # Data Cleaning
    # 1. Handle missing values
    df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].mean())

    # 2. Remove duplicate entries
    df = df.drop_duplicates()

    # Data Transformation
    # 1. Standard scaling of numerical columns
    scaler = StandardScaler()
    numeric_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
                      'total_bedrooms', 'population', 'households', 'median_income']
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    # 2. One-hot encoding for categorical columns
    df = pd.get_dummies(df, columns=['ocean_proximity'])

    # Data Reduction
    # 1. Remove highly correlated features (threshold = 0.8)
    correlation_matrix = df.corr().abs()
    upper = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] > 0.8)]
    df = df.drop(to_drop, axis=1)

    # 2. Remove low-variance features
    variance_threshold = 0.01
    variances = df.var()
    df = df[df.columns[variances > variance_threshold]]

    # Data Discretization
    # 1. Bin median_income into categories
    df['income_category'] = pd.qcut(df['median_income'],
                                  q=5,
                                  labels=['very_low', 'low', 'medium', 'high', 'very_high'])

    # 2. Bin housing_median_age into categories
    df['age_category'] = pd.cut(df['housing_median_age'],
                               bins=[0, 10, 20, 30, 40, np.inf],
                               labels=['very_new', 'new', 'medium', 'old', 'very_old'])

    # Save the preprocessed data
    output_path = '/home/doc-bd-a1/res_dpre.csv'
    df.to_csv(output_path, index=False)

    # Call the next script
    subprocess.run(['python3', 'eda.py', output_path])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py <dataset-path>")
        sys.exit(1)

    file_path = sys.argv[1]
    preprocess_data(file_path)
