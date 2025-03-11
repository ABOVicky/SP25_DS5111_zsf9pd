"""
factory.py

This module implements the Factory Design Pattern for
creating GainerDownload and GainerProcess instances.
"""

from bin.gainers.downloaders import GainerDownloadYahoo, GainerDownloadWSJ
from bin.gainers.processors import GainerProcessYahoo, GainerProcessWSJ

class GainerFactory:
    """Factory class to create Gainer objects"""

    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """Returns the correct downloader based on choice"""
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        return GainerDownloadWSJ()

    def get_processor(self):
        """Returns the correct processor based on choice"""
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        return GainerProcessWSJ()
