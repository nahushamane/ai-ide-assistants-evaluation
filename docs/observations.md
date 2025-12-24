## GitHub Copilot – Autocomplete (extract.py)

- Prompt: def extract_csv(file_path):
- Copilot generated full function with error handling
- Manual edits required: none
- Accuracy: High

## GitHub Copilot – Autocomplete (transform.py)

- Prompt: def transform_sales_data(df): """ - remove rows with null values - create total_amount = quantity * price - return cleaned dataframe """
- Generated pandas transformations correctly
- Handled arithmetic and filtering well
- Manual edits required: none
- Accuracy: High

## GitHub Copilot - Autocomplete (validation.py)

- Prompt: def validate_schema(df, expected_columns):
- Copilot initially assumed expected_columns as list
- Required clarification for dict-based schema
- Generated missing/extra columns list well

## GitHub Copilot - Chat Refactoring (extract.py)

- Prompt: Refactor this extraction code to be production-ready with logging and retries.
- Added logging and retries mechanism
- Added required libraries to the code
- Manual edits required: none
- Accuracy: High

## GitHub Copilot - SQL Assistance (analytics_queries.sql)

- Prompt: -- calculate total revenue per product -- include only completed orders -- order by revenue descending
- Copilot selected the correct colums, correctly summed the required columns, and wrote correct join and group conditions
- Manual edits required: none
- Accuracy: High

----------------------------------------------------------------------
----------------------------------------------------------------------

## Cursor – Context Handling Insight

- Cursor reliably reasons over explicitly opened files
- Repo-wide explanations require manual context exposure
- Highlighted importance of controlling AI context scope

