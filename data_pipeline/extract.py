import pandas as pd
import logging
import time

logger = logging.getLogger(__name__)

def extract_csv(file_path, retries=3, delay=1):
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.
    retries (int): Number of retry attempts on failure.
    delay (float): Delay in seconds between retries.

    Returns:
    pandas.DataFrame or None: The extracted data, or None if extraction fails after retries.
    """
    for attempt in range(retries):
        try:
            data = pd.read_csv(file_path)
            logger.info(f"Successfully extracted data from {file_path}")
            return data
        except FileNotFoundError as e:
            logger.error(f"File not found: {file_path}: {e}")
            raise  # Do not retry for file not found
        except pd.errors.EmptyDataError as e:
            logger.warning(f"Empty data in {file_path}: {e}")
            return pd.DataFrame()  # Return empty DataFrame for empty files
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed for {file_path}: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                logger.error(f"All {retries} retries exhausted for {file_path}")
                return None
    return None