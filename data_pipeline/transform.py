import pandas as pd

def transform_sales_data(df):
    """
    - remove rows with null values
    - create total_amount = quantity * price
    - return cleaned dataframe
    """
    try:
        # Remove rows with null values
        df_cleaned = df.dropna()

        # Create total_amount column
        df_cleaned['total_amount'] = df_cleaned['quantity'] * df_cleaned['price']

        return df_cleaned
    except Exception as e:
        print(f"An error occurred while transforming sales data: {e}")
        return None