import sys

from service.bts_scraper import BooksToScrapeScraper
from service.rate_limiter import SimpleRateLimiter
from service.books_list_csv_storage import BooksListCsvStorage

CSV_FIELD_SEPARATOR = ','
CSV_LINE_SEPARATOR = '\n'


def main():
    if len(sys.argv) != 4:
        print("Usage: main rate_limit_interval verbose file_name")
        print("example: main.py 1 0 /app/export/books.csv")
        exit(1)

    rate_limiter_interval_in_seconds = int(sys.argv[1])
    verbose = bool(sys.argv[2])
    csv_output_file = sys.argv[3]

    csv_writer = BooksListCsvStorage(csv_output_file, CSV_FIELD_SEPARATOR, CSV_LINE_SEPARATOR)

    rate_limiter = SimpleRateLimiter(rate_limiter_interval_in_seconds, verbose)
    scraper = BooksToScrapeScraper(rate_limiter, verbose)
    scraper.scrape()

    csv_writer.write(scraper.books)


if __name__ == '__main__':
    main()
