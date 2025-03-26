"""
processors.py

Contains concrete implementations of GainerProcess for Yahoo and WSJ.
"""

from bin.gainers.base import GainerProcess

class GainerProcessYahoo(GainerProcess):
    """Processes Yahoo gainers data"""

    def normalize(self):
        """Simulates normalizing Yahoo gainers"""
        print("Normalizing Yahoo gainers...")

    def save_with_timestamp(self):
        """Simulates saving Yahoo gainers with a timestamp"""
        print("Saving Yahoo gainers with timestamp...")

class GainerProcessWSJ(GainerProcess):
    """Processes WSJ gainers data"""

    def normalize(self):
        """Simulates normalizing WSJ gainers"""
        print("Normalizing WSJ gainers...")

    def save_with_timestamp(self):
        """Simulates saving WSJ gainers with a timestamp"""
        print("Saving WSJ gainers with timestamp...")
