from parse import parse_data
from settings import *
from callbacks import callbacks
import time
from summary import write_summary
from Levenshtein import *


def main():
    dblp_papers = 0
    mag_papers = 0

    start_time = time.time()
    if DBLP_parsing == True:
        dblp_papers = parse_data(DBLP_file_path, callbacks, DBLP_paper_count, 'DBLP')

    if MAG_parsing == True:
        mag_papers = parse_data(MAG_file_path, callbacks, MAG_paper_count, 'MAG')

    end_time = time.time() - start_time
    duration = f'{end_time // 60} minutes' if end_time > 60 else f'{end_time:.2f} seconds'

    if write_short_summary or write_long_summary:
        write_summary(duration, dblp_papers, mag_papers)


if __name__ == "__main__":
    main()