"""
get_gainer.py
# test
This script retrieves and processes stock gainers data
using the Factory and Template Design Patterns.
"""

import sys
from bin.gainers.factory import GainerFactory
from bin.gainers.process_gainer import ProcessGainer

def main():
    """Main function to process gainers"""

    if len(sys.argv) < 2:
        print("Usage: python get_gainer.py <source>")
        sys.exit(1)

    choice = sys.argv[1]

    # Use the Factory to get the correct downloader and processor
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # Create and run the process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()

if __name__ == "__main__":
    main()
