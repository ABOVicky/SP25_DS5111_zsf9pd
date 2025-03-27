"""
processors.py

Contains concrete implementations of GainerProcess for Yahoo and WSJ.
"""

from bin.gainers.base import GainerProcess
import datetime
import os

class GainerProcessYahoo(GainerProcess):
    """Processes Yahoo gainers data"""

    def normalize(self):
        """Simulates normalizing Yahoo gainers"""
        print("Normalizing Yahoo gainers...")

    def save_with_timestamp(self):
        """Saves Yahoo gainers to a timestamped CSV file"""
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = getattr(self, "output_filename", f"data/raw/yahoo_gainers_{now}.csv")
        print(f"Saving Yahoo gainers to {filename}")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("symbol,price,price_change,price_percent_change\n")
            f.write("AAPL,150,2.3,+1.5%\n")

class GainerProcessWSJ(GainerProcess):
    """Processes WSJ gainers data"""

    def normalize(self):
        """Simulates normalizing WSJ gainers"""
        print("Normalizing WSJ gainers...")

    def save_with_timestamp(self):
        """Saves WSJ gainers to a timestamped CSV file"""
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = getattr(self, "output_filename", f"data/raw/wsj_gainers_{now}.csv")
        print(f"Saving WSJ gainers to {filename}")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("symbol,price,price_change,price_percent_change\n")
            f.write("MSFT,310,4.5,+1.7%\n")
