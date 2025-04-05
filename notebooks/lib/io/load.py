import os 
import pandas as pd

def load_data(data_path="../data/"):
    """Load the credit scoring dataset."""
    # Check if the data directory exists
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data directory '{data_path}' not found.")
    
    # Look for CSV files in the data directory
    csv_files = [f for f in os.listdir(data_path) if f.endswith('train.csv')]
    
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in '{data_path}'.")
    
    # Load the first CSV file found
    file_path = os.path.join(data_path, csv_files[0])
    print(f"Loading data from: {file_path}")
    
    return pd.read_csv(file_path)
