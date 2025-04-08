"""
Unit tests for normalize_csv.py using pytest.
"""

import os
import sys
import pandas as pd
sys.path.append(".")
import bin.normalize_csv as nc

# Define test cases
TEST_FILES = ["sample_data/sample.csv", "sample_data/ygainers.csv"]

def test_normalize_csv():
    """Test the CSV normalization function on multiple test files""" # can we give it a go to use the Given/When/Then paradigm for writing test comments?

    for test_csv_path in TEST_FILES:
        # Ensure the test file exists
        assert os.path.exists(test_csv_path), f"Test file {test_csv_path} not found!"

        # Run normalization
        nc.normalize_csv(test_csv_path)

        # Check if the output file is created
        norm_csv_path = test_csv_path.replace('.csv', '_norm.csv')
        assert os.path.exists(norm_csv_path), f"Output file {norm_csv_path} not created!"

        # Read normalized file
        df = pd.read_csv(norm_csv_path)
        expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        
        # Check if expected columns are present
        assert all(col in df.columns for col in expected_columns), f"Columns missing in {norm_csv_path}"

        # Cleanup test artifacts
        os.remove(norm_csv_path)
