"""
downloaders.py

Contains concrete implementations of GainerDownload for Yahoo and WSJ.
"""

import os
from bin.gainers.base import GainerDownload

class GainerDownloadYahoo(GainerDownload):
    """Downloads Yahoo gainers data"""

    def download(self):
        """Downloads Yahoo gainers using headless Chrome"""
        print("Downloading Yahoo gainers...")
        os.system(
            "google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox "
            "--timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' "
            "> ygainers.html"
        )

    def __str__(self):
        return "Yahoo Gainer Downloader"

class GainerDownloadWSJ(GainerDownload):
    """Downloads WSJ gainers data"""

    def download(self):
        """Downloads WSJ gainers using headless Chrome"""
        print("Downloading WSJ gainers...")
        os.system(
            "google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox "
            "--timeout=5000 https://www.wsj.com/market-data/stocks/us/movers "
            "> wjsgainers.html"
        )

    def __str__(self):
        return "WSJ Gainer Downloader"
