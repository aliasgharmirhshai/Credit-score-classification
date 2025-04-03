import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def report_missing_data(df, dataset_name="Dataset"):
    """
    Reports missing data in a dataset with details and visualizations.
    
    Parameters:
    - df: pandas DataFrame - The dataset to analyze
    - dataset_name: str - Name of the dataset for reporting (default: "Dataset")
    
    Returns:
    - None: Prints results and displays visualizations
    """
    
    # Calculate total number of entries
    total_entries = df.size  # Total number of cells (rows * columns)
    total_rows = df.shape[0]
    total_cols = df.shape[1]
    
    # Identify variables with missing data
    missing_by_column = df.isnull().sum()  # Count of missing values per column
    missing_percent_by_column = (missing_by_column / total_rows) * 100  # Percentage per column
    
    # Filter to columns with missing data
    missing_columns = missing_by_column[missing_by_column > 0]
    missing_percent_columns = missing_percent_by_column[missing_by_column > 0]
    
    # Calculate total missing data
    total_missing = missing_by_column.sum()  # Total count of missing values
    total_missing_percent = (total_missing / total_entries) * 100  # Total percentage
    
    # Print report
    print(f"### Missing Data Report for {dataset_name} ###")
    print(f"Total Rows: {total_rows}, Total Columns: {total_cols}")
    print(f"Total Entries (cells): {total_entries}")
    print("\n#### Variables with Missing Data ####")
    if len(missing_columns) > 0:
        for col, count in missing_columns.items():
            percent = missing_percent_by_column[col]
            print(f"{col}: {count} missing values ({percent:.2f}%)")
    else:
        print("No missing data found in any variable.")
    
    print(f"\n#### Overall Missing Data ####")
    print(f"Total Missing Values: {total_missing}")
    print(f"Total Missing Percentage: {total_missing_percent:.2f}%")
    

    # Visualizations
    plt.figure(figsize=(12, 8))
    
    # Heatmap of missing data
    plt.subplot(2, 1, 1)
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title(f"Missing Data Heatmap - {dataset_name}")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    
    # Bar plot of missing data by column
    plt.subplot(2, 1, 2)
    missing_percent_columns.plot(kind='bar', color='skyblue')
    plt.title(f"Percentage of Missing Data by Variable - {dataset_name}")
    plt.xlabel("Variables")
    plt.ylabel("Percentage Missing (%)")
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()