import pandas as pd

# Data Preprocessing Steps:
# 1. Extracting unique values from rows with multiple values.
# 2. Creating tables containing extracted unique values as key-value pairs.
# 3. Expanding rows with multiple values into separate rows.

def extract_unique_values(df, column):
    """
    Extracts and returns unique values from a specified column in a DataFrame.
    
    Args:
    df (pd.DataFrame): The DataFrame to process.
    column (str): The name of the column from which to extract unique values.

    Returns:
    set: A set of unique values.
    """
    unique_vals = set()
    # Iterate over non-null values and update the set with unique values
    for val in df[column].dropna():
        unique_vals.update(val.split(','))
    return unique_vals

def create_dataframe_from_unique_values(unique_values):
    """
    Creates a DataFrame from a list of unique values with two columns: keys and values.

    Args:
    unique_values (list): A list of unique values.

    Returns:
    pd.DataFrame: A DataFrame with two columns - 'keys' and 'values'.
    """
    # Generate keys as a range of integers from 0 to the length of unique_values
    keys = range(len(unique_values))

    # Create the DataFrame
    df = pd.DataFrame({
        'keys': keys,
        'values': unique_values
    })

    return df


def expand(df, column_name):
    """
    Expands a DataFrame by splitting a specified column's multiple values into separate rows.

    Args:
    df (pd.DataFrame): The DataFrame to expand.
    column_name (str): The name of the column to expand.

    Returns:
    pd.DataFrame: An expanded DataFrame with separate rows for each value.
    """
    expanded_rows = []
    for _, row in df.iterrows():
        vals = row[column_name]
        exp_list = vals.split(',') if isinstance(vals, str) else [None]

        for val in exp_list:
            new_row = row.to_dict()
            new_row[column_name] = val
            expanded_rows.append(new_row)

    expanded_df = pd.DataFrame(expanded_rows)
    expanded_df.drop_duplicates(inplace=True)
    expanded_df.reset_index(drop=True, inplace=True)
    return expanded_df
