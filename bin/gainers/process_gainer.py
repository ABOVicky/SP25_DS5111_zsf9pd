"""
process_gainer.py

Implements the Template Method Pattern for processing gainers.
"""

class ProcessGainer:
    """Handles downloading, processing, and saving gainers data"""

    def __init__(self, gainer_downloader, gainer_normalizer):
        """Initializes the ProcessGainer with a downloader and processor"""
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        """Triggers the download process"""
        self.downloader.download()

    def _normalize(self):
        """Triggers the normalization process"""
        self.normalizer.normalize()

    def _save_to_file(self):
        """Triggers saving the processed data"""
        self.normalizer.save_with_timestamp()

    def process(self):
        """Runs the full process"""
        self._download()
        self._normalize()
        self._save_to_file()

    def __str__(self):
        """String representation"""
        return "ProcessGainer Pipeline"
