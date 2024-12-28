import pandas as pd

def csv_to_sql_insert(input_csv, table_name, output_file):
    """
    Converts a CSV file into SQL INSERT statements and saves the result to a file.

    Parameters:
        input_csv (str): Path to the input CSV file.
        table_name (str): Name of the SQL table for the INSERT statements.
        output_file (str): Path to the output file where SQL statements will be saved.

    Returns:
        None: Saves the SQL INSERT statements to the output file.
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)
    
    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Write the INSERT header
        columns = ", ".join(df.columns)
        file.write(f"INSERT INTO {table_name} ({columns}) VALUES\n")
        
        # Build SQL tuples for each row
        rows = []
        for _, row in df.iterrows():
            # Format each value in the row
            values = []
            for value in row:
                # Handle strings and escape single quotes
                if isinstance(value, str):
                    values.append(f"'{value.replace("'", "''")}'")
                # Handle null values
                elif pd.isnull(value):
                    values.append("NULL")
                # Handle datetime values
                elif isinstance(value, pd.Timestamp):
                    values.append(f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'")
                # Handle numbers (int or float)
                elif isinstance(value, (int, float)):
                    values.append(str(value))
                # Handle any other types by converting them to strings
                else:
                    values.append(f"'{str(value).replace('\'', '\'\'')}'")
            # Create a SQL tuple for the current row
            rows.append(f"({', '.join(values)})")
        
        # Write all rows to the file, separated by commas, and close with a semicolon
        file.write(",\n".join(rows) + ";")
    
    print(f"The file '{output_file}' has been successfully generated with SQL commands.")

# Exmaple usage
input_csv = 'input.csv'
table_name = 'users'
output_file = 'inser_values_users.sql'

csv_to_sql_insert(input_csv, table_name, output_file)