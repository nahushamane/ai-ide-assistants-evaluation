import pandas as pd

def validate_schema(df, expected_columns):
    """
    Validates that the DataFrame contains the expected columns.

    Parameters:
    df (pandas.DataFrame): The DataFrame to validate.
    expected_columns (list): A list of expected column names.

    Returns:
    bool: True if the DataFrame contains all expected columns, False otherwise.
    """
    try:
        df_columns = set(df.columns)
        expected_columns_set = set(expected_columns)

        if df_columns == expected_columns_set:
            return True
        else:
            missing_columns = expected_columns_set - df_columns
            extra_columns = df_columns - expected_columns_set
            if missing_columns:
                print(f"Missing columns: {missing_columns}")
            if extra_columns:
                print(f"Extra columns: {extra_columns}")
            return False
    except Exception as e:
        print(f"An error occurred while validating schema: {e}")
        return False