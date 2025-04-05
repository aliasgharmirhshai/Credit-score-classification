import pandas as pd
import numpy as np

def drop_columns(df, columns_to_drop):
    # Drop columns, ignoring errors if a column does not exist
    df = df.drop(columns=columns_to_drop, axis=1, errors='ignore')

    # Verify and print confirmation for dropped columns
    for col in columns_to_drop:
        if col not in df.columns:
            print(f"Column '{col}' dropped successfully.")

    return df  


def transform_data_types(df):
    """
    Transforms the data types of specified columns in the DataFrame and cleans the 'Age' column.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to be transformed.
    
    Returns:
    pd.DataFrame: The transformed DataFrame with corrected data types and cleaned 'Age' column.
    """
    # Annual_Income: remove non-numeric characters except '.', convert to float
    df['Annual_Income'] = df['Annual_Income'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float)
    
    # Num_of_Loan: convert to numeric, fill NaN with 0, convert to int
    df['Num_of_Loan'] = pd.to_numeric(df['Num_of_Loan'], errors='coerce').fillna(0).astype(int)
    
    # Num_of_Delayed_Payment: similar to Num_of_Loan
    df['Num_of_Delayed_Payment'] = pd.to_numeric(df['Num_of_Delayed_Payment'], errors='coerce').fillna(0).astype(int)
    
    # Changed_Credit_Limit: convert to numeric, coerce errors to NaN
    df['Changed_Credit_Limit'] = pd.to_numeric(df['Changed_Credit_Limit'], errors='coerce')
    
    # Outstanding_Debt: remove non-numeric characters except '.', convert to float
    df['Outstanding_Debt'] = df['Outstanding_Debt'].str.replace(r'[^\d.]', '', regex=True).astype(float)
    
    # Amount_invested_monthly: convert to numeric, coerce errors to NaN
    df['Amount_invested_monthly'] = pd.to_numeric(df['Amount_invested_monthly'], errors='coerce')
    
    # Monthly_Balance: convert to numeric, coerce errors to NaN
    df['Monthly_Balance'] = pd.to_numeric(df['Monthly_Balance'], errors='coerce')
    
    # Age: convert to numeric, coerce errors to NaN
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    
    # Compute median of non-NaN ages, default to 0 if all NaN
    age_median = int(df['Age'].median()) if not df['Age'].isna().all() else 0
    
    # Fill NaN with median and convert to int
    df['Age'] = df['Age'].fillna(age_median).astype(int)
    
    # Compute median of non-negative ages, default to 0 if no non-negative ages
    median_age = int(df[df['Age'] >= 0]['Age'].median()) if not df[df['Age'] >= 0].empty else 0
    
    # Replace negative ages with median_age
    df['Age'] = df['Age'].apply(lambda x: median_age if x < 0 else x).astype(int)
    
    # Drop rows where Age > 100 or Age < 0
    df = df[(df['Age'] >= 0) & (df['Age'] <= 100)]
    
    return df

def clean_categorical(df):
    """
    Cleans and standardizes Categorical columns in the DataFrame for a data pipeline.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to be cleaned.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Create a copy to avoid modifying the original DataFrame
    cleaned_df = df.copy()
    
    # Clean 'Occupation'
    cleaned_df['Occupation'] = cleaned_df['Occupation'].replace("_______", "Unknown")
    cleaned_df['Occupation'] = cleaned_df['Occupation'].str.title().str.strip()
    
    # Clean 'Credit_Mix'
    cleaned_df['Credit_Mix'] = cleaned_df['Credit_Mix'].fillna("Unknown")
    cleaned_df['Credit_Mix'] = cleaned_df['Credit_Mix'].replace("_", "Unknown")
    cleaned_df['Credit_Mix'] = cleaned_df['Credit_Mix'].str.title().str.strip()
    
    # Clean 'Payment_of_Min_Amount'
    cleaned_df['Payment_of_Min_Amount'] = cleaned_df['Payment_of_Min_Amount'].fillna("Unknown")
    cleaned_df['Payment_of_Min_Amount'] = cleaned_df['Payment_of_Min_Amount'].replace("NM", "Unknown")
    cleaned_df['Payment_of_Min_Amount'] = cleaned_df['Payment_of_Min_Amount'].str.title().str.strip()
    
    # Clean 'Payment_Behaviour'
    cleaned_df['Payment_Behaviour'] = cleaned_df['Payment_Behaviour'].fillna("Unknown")
    cleaned_df['Payment_Behaviour'] = cleaned_df['Payment_Behaviour'].replace("!@9#%8", "Unknown")
    cleaned_df['Payment_Behaviour'] = cleaned_df['Payment_Behaviour'].str.replace("_", " ").str.title().str.strip()
    
    # Define mapping for Payment_Behaviour
    duplicate_mapping = {
        "Low Spent Small": "Low Spent Small Value Payments",
        "High Spent Small": "High Spent Small Value Payments",
        "Low Spent Large": "Low Spent Large Value Payments",
        "Low Spent Medium": "Low Spent Medium Value Payments",
        "High Spent Medium": "High Spent Medium Value Payments",
        "High Spent Large": "High Spent Large Value Payments",
        "Unknown": "Unknown"
    }
    cleaned_df['Payment_Behaviour'] = cleaned_df['Payment_Behaviour'].replace(duplicate_mapping)
    
    # Clean 'Credit_Score' if it exists
    if 'Credit_Score' in cleaned_df.columns:
        cleaned_df['Credit_Score'] = cleaned_df['Credit_Score'].str.strip().str.title()
    
    return cleaned_df


def transform_special_columns(df):
    """
    Transforms specific columns in the DataFrame for a data pipeline.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to be transformed.
    
    Returns:
    pd.DataFrame: The transformed DataFrame.
    """
    # Month transformation: Map month names to numbers and handle invalid values
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    month_mapping = {month: i for i, month in enumerate(month_order, start=1)}
    df['Month'] = df['Month'].map(month_mapping).fillna(0).astype(int)
    
    # Credit_History_Age transformation: Convert string to total months
    def convert_to_months(age_str):
        if pd.isna(age_str):
            return np.nan
        try:
            parts = age_str.split()
            years = int(parts[0])
            months = int(parts[3])
            total_months = (years * 12) + months
            return total_months
        except (IndexError, ValueError):
            return np.nan
    
    df['Credit_History_Age'] = df['Credit_History_Age'].apply(convert_to_months).astype(float)
    
    # Type_of_Loan transformation: Standardize format
    df['Type_of_Loan'] = df['Type_of_Loan'].apply(
        lambda x: x.lower().replace('and ', '').replace(', ', ',').strip() if pd.notna(x) else x
    )
    
    return df

def handle_missing_data(df):
    """
    Handles missing data for specific columns in the DataFrame for use in a data pipeline.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to be processed.
    
    Returns:
    pd.DataFrame: A new DataFrame with missing values handled.
    """
    # Create a copy to avoid modifying the original DataFrame
    df_copy = df.copy()
    
    # Handle 'Type_of_Loan' (categorical) by filling with "Unknown"
    df_copy['Type_of_Loan'] = df_copy['Type_of_Loan'].fillna("Unknown")
    
    # Define numerical columns to impute with their respective medians
    numerical_cols = [
        'Credit_History_Age',
        'Monthly_Inhand_Salary',
        'Changed_Credit_Limit',
        'Num_Credit_Inquiries',
        'Amount_invested_monthly',
        'Monthly_Balance'
    ]
    
    # Impute missing values with median for each numerical column
    for col in numerical_cols:
        median_value = df_copy[col].median()
        df_copy[col] = df_copy[col].fillna(median_value)
    
    return df_copy