"""
CSV Normalization Script

This script reads raw CSV files, standardizes column names, and outputs a normalized CSV.
"""

import os
import sys
import pandas as pd

def normalize_csv(input_csv_path):
    """
    Reads a CSV file, normalizes its column names, and saves a new CSV file with `_norm` appended.
    """
    assert isinstance(input_csv_path, str), f"Expected string, got {type(input_csv_path)}"
    assert os.path.exists(input_csv_path), f"File not found: {input_csv_path}"

    # Read CSV
    df = pd.read_csv(input_csv_path)

    # Define Expected Headers
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']

    # Map Column Names from Different Sources to Standard Names
    column_mapping = {
        'Symbol': 'symbol', 'Ticker': 'symbol',
        'Price': 'price', 'Last Price': 'price',
        'Change': 'price_change', 'Price Change': 'price_change',
        'Change %': 'price_percent_change', 'Percent Change': 'price_percent_change',
        '% Change': 'price_percent_change'
    }

    # Rename Columns (Based on Mapping)
    df.rename(columns=column_mapping, inplace=True)

    # Ensure Only Expected Columns are Present
    df = df[[col for col in expected_columns if col in df.columns]]

    # Output File Path
    output_csv_path = input_csv_path.replace('.csv', '_norm.csv')

    # Save New File
    df.to_csv(output_csv_path, index=False)

    print(f"Normalized CSV saved as: {output_csv_path}")

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: python bin/normalize_csv.py <input_csv_path>"
    normalize_csv(sys.argv[1])
