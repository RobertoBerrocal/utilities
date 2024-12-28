import pandas as pd
import os
from tqdm import tqdm

def split_csv_by_parts(file_name, num_parts, encoding='utf-8'):
    """
    Splits a large CSV file into a specified number of smaller files.

    Parameters:
        file_name (str): The path to the original CSV file.
        num_parts (int): The number of smaller files to create.
        encoding (str): The encoding of the CSV file. Default is 'utf-8'.

    Returns:
        None
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_name, encoding=encoding)
    except UnicodeDecodeError as e:
        print(f"Encoding error while reading the file: {e}")
        return
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # Calculate the number of rows per file
    rows_per_file = len(df) // num_parts + (1 if len(df) % num_parts > 0 else 0)
    
    # Extract the base name and extension of the file
    base_name, extension = os.path.splitext(file_name)
    
    # Split and save the files with a progress bar
    print(f"Splitting into {num_parts} files...")
    for i in tqdm(range(num_parts), desc="Splitting CSV"):
        start_idx = i * rows_per_file
        end_idx = min(start_idx + rows_per_file, len(df))
        
        temp_df = df.iloc[start_idx:end_idx]
        new_file_name = f"{base_name}_part_{i+1}{extension}"
        temp_df.to_csv(new_file_name, index=False, encoding=encoding)
    
    print("CSV split completed!")

# Example
split_csv_by_parts('./kidney_disease.csv', 5, encoding='utf-8')