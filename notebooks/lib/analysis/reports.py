import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def categorical_summary_stats(df, categorical_columns=None):
    """
    Generate summary statistics for categorical variables in a dataframe.
    
    Parameters:
    df (pandas.DataFrame): The dataframe to analyze
    categorical_columns (list, optional): List of categorical column names to analyze.
                                         If None, will try to identify categorical columns.
    
    Returns:
    dict: Dictionary where keys are column names and values are dictionaries of summary statistics
    """    
    # If no categorical columns specified, try to identify them
    if categorical_columns is None:
        # Select object, category, and boolean dtypes
        categorical_columns = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
        
        # Also include numeric columns with low cardinality (fewer than 10 unique values)
        for col in df.select_dtypes(include=['number']).columns:
            if df[col].nunique() < 10:
                categorical_columns.append(col)
    
    summary = {}
    
    for col in categorical_columns:
        if col not in df.columns:
            continue
            
        # Basic stats
        value_counts = df[col].value_counts()
        unique_values = df[col].unique()
        missing_values = df[col].isna().sum()
        
        # Get mode (most frequent value)
        mode_value = df[col].mode()[0] if not df[col].empty else None
        mode_count = value_counts.iloc[0] if not value_counts.empty else 0
        mode_percentage = (mode_count / len(df)) * 100 if len(df) > 0 else 0
        
        # Get top 5 categories with counts and percentages
        top_categories = []
        for value, count in value_counts.head(5).items():
            percentage = (count / len(df)) * 100
            top_categories.append({
                'value': value,
                'count': count,
                'percentage': round(percentage, 2)
            })
        
        # Compile column summary
        summary[col] = {
            'unique_values': len(unique_values),
            'missing_values': missing_values,
            'missing_percentage': round((missing_values / len(df)) * 100, 2) if len(df) > 0 else 0,
            'mode': {
                'value': mode_value,
                'count': mode_count,
                'percentage': round(mode_percentage, 2)
            },
            'top_categories': top_categories,
            'all_categories': [str(v) for v in unique_values]
        }
    
    return summary


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