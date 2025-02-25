import sys
import platform

def test_os_is_linux():
    """Ensure the tests are running on a Linux machine"""
    assert platform.system() == "Linux", f"Tests must be run on Linux, found: {platform.system()}"

def test_python_version():
    """Ensure the Python version is 3.10 or 3.11"""
    major, minor = sys.version_info[:2]
    assert (major, minor) in [(3, 10), (3, 11)], f"Python version must be 3.10 or 3.11, found: {major}.{minor}"
