from lib.preprocessing.cleaning import (
    drop_columns,
    transform_data_types,
    clean_categorical,
    transform_special_columns,
    handle_missing_data
)
from lib.io.load import load_data
import os
import pandas as pd  # Add this import if not already present

def process_and_save(file_name, output_name):
    # Construct the absolute path for the input file
    data_dir = os.path.join(os.path.dirname(__file__), "data/raw")
    file_path = os.path.join(data_dir, file_name)

    # Explicitly set low_memory=False to avoid DtypeWarning
    df = pd.read_csv(file_path, low_memory=False)
    print("-----")

    columns_to_drop = [
        "ID",
        "Name",  
        "SSN",  
        "Customer_ID",  
    ]
    df = drop_columns(df, columns_to_drop)
    print("drops the columns ✅")

    print("-----")
    df = transform_data_types(df)
    print("Transforms the data types ✅")

    print("-----")
    df = clean_categorical(df)
    print("cleans the categorical columns ✅")

    print("-----")
    df = transform_special_columns(df)
    print("Transforms special columns ✅")

    print("-----")
    df = handle_missing_data(df)
    print("Handles missing data ✅")

    # Save the cleansed data to the 'processed' directory
    processed_dir = os.path.join(os.path.dirname(__file__), "data/processed")
    os.makedirs(processed_dir, exist_ok=True)
    output_path = os.path.join(processed_dir, output_name)
    df.to_csv(output_path, index=False)
    print("-----")
    print(f"Cleansed data saved to {output_path} ✅")

if __name__ == "__main__":
    process_and_save("train.csv", "train_processed.csv")
    process_and_save("test.csv", "test_processed.csv")