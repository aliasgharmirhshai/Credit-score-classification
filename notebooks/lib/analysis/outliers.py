from scipy.stats import zscore
import numpy as np

def calculate_zscore_outliers(column, threshold=3):
    """
    Calculate the number and percentage of outliers in a column using Z-Score.

    Parameters:
    - column (array-like): A numerical data column (e.g., a list or a pandas Series).
    - threshold (float): The Z-score threshold to determine outliers (default is 3).

    Returns:
    - count (int): The count of outlier values.
    - percentage (float): The percentage of outlier values in the column.
    """
    # Calculate the Z-Scores of the column
    z_scores = zscore(column)
    
    # Identify outliers where the absolute Z-Score exceeds the threshold
    outlier_mask = np.abs(z_scores) > threshold
    
    # Count the number of outliers
    count = np.sum(outlier_mask)
    
    # Calculate the percentage of outliers
    percentage = (count / len(column)) * 100
    
    return count, percentage


