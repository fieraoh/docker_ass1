# Team Members

- Abdullah Fathy | 19200112
- Mohammed Salah | 202001104

# Big Data Processing Pipeline Project

This project implements a data processing pipeline using Docker and Python for the Housing dataset. The pipeline includes data loading, preprocessing, exploratory data analysis, visualization, and K-means clustering.

## Directory Structure
```
bd-a1/
│
├── Dockerfile
├── housing.csv
├── service-result/
│   ├── res_dpre.csv
│   ├── eda-in-1.txt
│   ├── eda-in-2.txt
│   ├── eda-in-3.txt
│   ├── vis.png
│   └── k.txt
│
├── final.sh
└── README.md
```

## Prerequisites
- Docker Desktop installed and running
- Git (for version control)
- Text editor (VS Code recommended)

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd bd-a1
```

2. Download the Iris dataset:
```powershell
# Using PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv" -OutFile "housing.csv"
```

## Docker Commands Used

1. Build the Docker image:
```bash
docker build -t bd-processing .
```

2. Run the container:
```bash
docker run -it --name bd-container bd-processing
```

3. Copy files into the container (if needed):
```bash
docker cp <file> bd-container:/home/doc-bd-a1/
```

## Project Files Description

### Python Scripts
1. `load.py`:
   - Reads dataset dynamically
   - Accepts file path as argument
   - Triggers the preprocessing step

2. `dpre.py`:
   - Performs data cleaning
   - Handles data transformation
   - Implements data reduction
   - Applies data discretization
   - Saves output as res_dpre.csv

3. `eda.py`:
   - Generates 3 insights
   - Creates eda-in-1.txt, eda-in-2.txt, eda-in-3.txt

4. `vis.py`:
   - Creates visualization
   - Saves output as vis.png

5. `model.py`:
   - Implements K-means clustering (k=3)
   - Saves cluster information in k.txt

### Shell Script
- `final.ps1`: Copies results from container to local machine

## Pipeline Execution

1. Inside the container, run:
```bash
python3 load.py /home/doc-bd-a1/housing.csv
```

2. On local machine, execute:
```bash
chmod +x final.sh
./final.sh
```

## Docker Hub Deployment

1. Tag the image:
```bash
docker tag bd-processing <your-dockerhub-username>/bd-processing:latest
```

2. Push to Docker Hub:
```bash
docker login
docker push <your-dockerhub-username>/bd-processing:latest
```

## Project Tasks Overview

1. Data Preprocessing:
   - Data Cleaning: Handling missing values, removing duplicates
   - Data Transformation: Standardization, encoding
   - Data Reduction: Feature selection
   - Data Discretization: Binning numerical features

2. Exploratory Data Analysis:
   - Statistical analysis
   - Distribution analysis
   - Missing value analysis

3. Visualization:
   - Correlation heatmap

4. Modeling:
   - K-means clustering with k=3
   - Cluster size analysis
