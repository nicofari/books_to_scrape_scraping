from service.bts_scraper import BooksToScrapeScraper
from service.rate_limiter import SimpleRateLimiter

def main():

    RATE_LIMITER_INTERVAL_IN_SECONDS = 1
    RATE_LIMITER_VERBOSE = True

    rate_limiter = SimpleRateLimiter(RATE_LIMITER_INTERVAL_IN_SECONDS, RATE_LIMITER_VERBOSE)
    scraper = BooksToScrapeScraper(rate_limiter)
    scraper.scrape()

if __name__ == '__main__':
    main()