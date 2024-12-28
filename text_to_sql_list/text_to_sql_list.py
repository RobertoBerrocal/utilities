def csv_to_sql_list(input_file, is_number=False):
    """
    Converts the rows of a text or CSV file into a SQL-compatible list format and saves the result
    to a file named as the input file with "_sql_list" appended to its name.

    Parameters:
        input_file (str): Path to the input text or CSV file.
        is_number (bool): Whether the rows contain numeric values (default: False).

    Returns:
        None: Saves the SQL-compatible list to the output file.
    """
    # Generate the output file name
    output_file = f"{input_file.split('.')[0]}_sql_list.txt"

    # Read the input file
    with open(input_file, "r") as file:
        rows = file.read().splitlines()  # Read lines and remove newline characters

    # Format the rows into a SQL list
    if is_number:
        sql_list = tuple(map(int, rows))  # Convert rows to integers
    else:
        sql_list = tuple(f'{row}' for row in rows)  # Keep rows as strings with single quotes

    # Convert the tuple to a string suitable for SQL
    sql_list_str = str(sql_list)

    # Save the SQL list to the output file
    with open(output_file, "w") as file:
        file.write(sql_list_str)

    print(f"SQL list saved to {output_file}:")
    print("")
    print(sql_list_str)

# test the function with a text file with numbers
    csv_to_sql_list(input_file='input_text.txt', is_number=True)
# test the function with a text file with strings
    csv_to_sql_list(input_file='input_text.txt', is_number=False)