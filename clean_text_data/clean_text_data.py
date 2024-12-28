import pandas as pd
import re
import unicodedata

def clean_text(text):
    """
    Cleans a given text by:
    - Removing leading/trailing spaces
    - Removing all whitespace characters (spaces, tabs, newlines)
    - Converting to lowercase
    - Normalizing (removing accents/diacritics)
    - Removing unwanted characters while keeping specified special characters (e.g., #, $, @)

    Parameters:
        text (str): The input text to clean.

    Returns:
        str: The cleaned text.
    """
    if not isinstance(text, str):
        return text  # Return original value if not a string

    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Replace all types of whitespace (spaces, tabs, newlines) with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Normalize and remove accents/diacritics
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    
    # Define the allowed special characters
    allowed_special_chars = "#@$."  # Add or remove characters here as needed
    
    # Remove all characters except letters, numbers, spaces, and allowed special characters
    pattern = rf'[^a-z0-9áéíóúüñ {allowed_special_chars}]'
    text = re.sub(pattern, '', text)
    
    return text

def clean_text_column(df, column_name):
    """
    Cleans the text of a specific column in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The column to clean.

    Returns:
        pd.Series: The cleaned column as a pandas Series.
    """
    if column_name not in df.columns:
        raise ValueError(f"The column '{column_name}' does not exist in the DataFrame.")
    
    # Apply the clean_text function to the specified column 
    return df[column_name].apply(clean_text)

# Example
text = "¡Hola!  Soy   Roberto. \t ¿Cómo estás? Mi email es robberrocal@gmail.com"

print(clean_text(text))