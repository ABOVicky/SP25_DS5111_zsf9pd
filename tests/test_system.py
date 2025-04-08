import sys
import platform
import pytest
from bin.gainers.factory import GainerFactory
from bin.gainers.process_gainer import ProcessGainer
from bin.gainers.downloaders import GainerDownloadYahoo, GainerDownloadWSJ
from bin.gainers.processors import GainerProcessYahoo, GainerProcessWSJ

def test_os_is_linux():
    """Ensure the tests are running on a Linux machine"""
    assert platform.system() == "Linux", f"Tests must be run on Linux, found: {platform.system()}"

def test_python_version(): # head's up that this will have to change after updating the validations.yaml github action file
    """Ensure the Python version is 3.10 or 3.11"""
    major, minor = sys.version_info[:2]
    assert (major, minor) in [(3, 10), (3, 11), (3, 12)], f"Python version must be 3.10 -  3.12, found: {major}.{minor}"

def test_factory_yahoo():
    """Test that the Factory correctly returns a Yahoo Gainer downloader"""
    factory = GainerFactory("yahoo")
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    assert isinstance(downloader, GainerDownloadYahoo)
    assert isinstance(processor, GainerProcessYahoo)

def test_factory_wsj():
    """Test that the Factory correctly returns a WSJ Gainer downloader"""
    factory = GainerFactory("wsj")
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    assert isinstance(downloader, GainerDownloadWSJ)
    assert isinstance(processor, GainerProcessWSJ)

def test_process_gainer_yahoo():
    """Test the entire Yahoo Gainer process"""
    factory = GainerFactory("yahoo")
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    process = ProcessGainer(downloader, processor)

    assert process.downloader is not None
    assert process.normalizer is not None

def test_process_gainer_wsj():
    """Test the entire WSJ Gainer process"""
    factory = GainerFactory("wsj")
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    process = ProcessGainer(downloader, processor)

    assert process.downloader is not None
    assert process.normalizer is not None
