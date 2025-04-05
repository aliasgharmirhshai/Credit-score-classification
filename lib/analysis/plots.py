import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def create_correlation_heatmap(df, columns=None, method='pearson', figsize=(12, 10), 
                               cmap='coolwarm', annot=True, mask_upper=False, 
                               save_path=None):
    """
    Create a correlation heatmap to visualize relationships between variables in a dataset.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset to analyze
    columns : list or None, optional (default=None)
        List of column names to include in the correlation analysis. 
        If None, all numeric columns will be used.
    method : str, optional (default='pearson')
        Method of correlation:
        - 'pearson' : standard correlation coefficient
        - 'kendall' : Kendall Tau correlation coefficient
        - 'spearman' : Spearman rank correlation coefficient
    figsize : tuple, optional (default=(12, 10))
        Figure size (width, height) in inches
    cmap : str, optional (default='coolwarm')
        Colormap for the heatmap
    annot : bool, optional (default=True)
        If True, write the correlation value in each cell
    mask_upper : bool, optional (default=False)
        If True, mask the upper triangle of the correlation matrix
    save_path : str or None, optional (default=None)
        Path to save the figure. If None, the figure will be displayed but not saved.
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure object containing the heatmap
    corr_matrix : pandas.DataFrame
        The correlation matrix
    """
    # If no columns specified, use all numeric columns
    if columns is None:
        # Select only numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
    else:
        numeric_df = df[columns].select_dtypes(include=[np.number])
    
    # Calculate the correlation matrix
    corr_matrix = numeric_df.corr(method=method)
    
    # Create a mask for the upper triangle if required
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool)) if mask_upper else None
    
    # Set up the matplotlib figure
    plt.figure(figsize=figsize)
    
    # Draw the heatmap with the mask and correct aspect ratio
    fig = plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, mask=mask, cmap=cmap, annot=annot, 
                square=True, linewidths=.5, cbar_kws={"shrink": .5},
                fmt='.2f', annot_kws={"size": 8})
    
    plt.title(f'Correlation Matrix ({method.capitalize()} Method)', fontsize=16, pad=20)
    plt.tight_layout()
    
    # Save the figure if path is provided
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    
    return fig, corr_matrix


def visualize_outliers(df, columns=None, figsize=(12, 8), save_path=None):
    """
    Create boxplots to visualize outliers in the specified columns of a dataframe.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset to analyze
    columns : list or None, optional (default=None)
        List of column names to plot. If None, all numeric columns will be used.
    figsize : tuple, optional (default=(12, 8))
        Figure size (width, height) in inches
    save_path : str or None, optional (default=None)
        Path to save the figure. If None, the figure will be displayed but not saved.
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure object containing the boxplots
    """
    # If no columns specified, use all numeric columns
    if columns is None:
        columns = df.select_dtypes(include=['number']).columns.tolist()
    
    # Create the figure and subplots
    fig, axes = plt.subplots(len(columns), 1, figsize=figsize)
    
    # If only one column, axes won't be an array, so we convert it to a list
    if len(columns) == 1:
        axes = [axes]
    
    # Plot each column
    for i, column in enumerate(columns):
        sns.boxplot(x=df[column], ax=axes[i])
        axes[i].set_title(f'Boxplot of {column}')
        axes[i].set_xlabel('')
        
        # Add grid lines for better readability
        axes[i].grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    # Save the figure if path is provided
    if save_path:
        plt.savefig(save_path)
    
    return fig