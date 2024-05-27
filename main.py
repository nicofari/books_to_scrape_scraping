import sys

from service.bts_scraper import BooksToScrapeScraper
from service.rate_limiter import SimpleRateLimiter
from service.books_list_csv_storage import BooksListCsvStorage

CSV_FIELD_SEPARATOR = ','
CSV_LINE_SEPARATOR = '\n'


def main():
    if len(sys.argv) != 6:
        print("Usage: main rate_limit_interval verbose file_name from_page to_page")
        print("example: main.py 1 0 /app/export/books.csv 1 50")
        exit(1)

    rate_limiter_interval_in_seconds = int(sys.argv[1])
    verbose = bool(sys.argv[2])
    csv_output_file = sys.argv[3]
    from_page = int(sys.argv[4])
    to_page = int(sys.argv[5]) + 1

    csv_writer = BooksListCsvStorage(csv_output_file, CSV_FIELD_SEPARATOR, CSV_LINE_SEPARATOR)

    rate_limiter = SimpleRateLimiter(rate_limiter_interval_in_seconds, verbose)
    scraper = BooksToScrapeScraper(rate_limiter, verbose)
    scraper.scrape(from_page, to_page)

    csv_writer.write(scraper.books)


if __name__ == '__main__':
    main()
