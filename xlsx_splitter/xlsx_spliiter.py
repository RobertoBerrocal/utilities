import pandas as pd
import os
from tqdm import tqdm

def split_excel_by_parts(file_name, num_parts):
    """
    Splits a large Excel file into a specified number of smaller files.

    Parameters:
        file_name (str): The path to the original Excel file.
        num_parts (int): The number of smaller files to create.

    Returns:
        None
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_name)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # Calculate the number of rows per file
    rows_per_file = len(df) // num_parts + (1 if len(df) % num_parts > 0 else 0)
    
    # Extract the base name and extension of the file
    base_name, extension = os.path.splitext(file_name)
    
    # Split and save the files with a progress bar
    print(f"Splitting into {num_parts} files...")
    for i in tqdm(range(num_parts), desc="Splitting Excel"):
        start_idx = i * rows_per_file
        end_idx = min(start_idx + rows_per_file, len(df))
        
        temp_df = df.iloc[start_idx:end_idx]
        new_file_name = f"{base_name}_part_{i+1}.xlsx"
        temp_df.to_excel(new_file_name, index=False)
    
    print("Excel split completed!")