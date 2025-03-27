#!/usr/bin/env python3

import sys
import datetime
from bin.gainers.factory import GainerFactory
from bin.gainers.process_gainer import ProcessGainer

def main():
    if len(sys.argv) < 2:
        print("Usage: python collect_gainers.py <source>")
        sys.exit(1)

    choice = sys.argv[1]
    if choice not in ['yahoo', 'wsj']:
        print("Source must be 'yahoo' or 'wsj'")
        sys.exit(1)

    # Generate Timestamped Filenames to Avoid Overwriting
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    print(f"[INFO] Running data collection at {now} for source: {choice}")

    # Run Existing Process
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    # Optionally Modify Processor to Write to Timestamped File
    processor.output_filename = f"data/raw/{choice}_gainers_{now}.csv"

    runner = ProcessGainer(downloader, processor)
    runner.process()

if __name__ == "__main__":
    main()
