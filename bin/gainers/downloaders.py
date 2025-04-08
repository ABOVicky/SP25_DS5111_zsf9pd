"""
downloaders.py

Contains concrete implementations of GainerDownload for Yahoo and WSJ.
"""

from bin.gainers.base import GainerDownload

class GainerDownloadYahoo(GainerDownload):
    """Downloads Yahoo gainers data"""

    def download(self):
        """Simulates downloading Yahoo gainers""" # as mentioned in class we can update this by simply copying the bash code from the makefile
                                                  # and running it in os.system(<code from bash>).  That will make this functional for our purposes
        print("Downloading Yahoo gainers...")

    def __str__(self):
        """String representation"""
        return "Yahoo Gainer Downloader"

class GainerDownloadWSJ(GainerDownload):
    """Downloads WSJ gainers data"""

    def download(self):
        """Simulates downloading WSJ gainers"""
        print("Downloading WSJ gainers...")

    def __str__(self):
        """String representation"""
        return "WSJ Gainer Downloader"
