import requests
from service.bts_parser import BooksToScrapeSitePageParser


class BooksToScrapeScraper:
    URL_TEMPLATE = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

    REFERER = "https://books.toscrape.com/"
    ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
    ACCEPT_LANGUAGE = "en-US,en;q=0.6"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    def __init__(self, rate_limiter, verbose):
        self.books = []
        self.rate_limiter = rate_limiter
        self.verbose = verbose

    def scrape(self, from_page, to_page):
        custom_headers = {
            "User-Agent": self.USER_AGENT,
            "Accept": self.ACCEPT,
            "Accept-Language": self.ACCEPT_LANGUAGE,
            "Referer": self.REFERER
        }

        for page in range(from_page, to_page):
            url = self.URL_TEMPLATE.format(page)

            print(f'Get page {page}')

            try:
                response = requests.get(url, headers=custom_headers)
                response.encoding = 'UTF-8'

            except Exception as ex:
                print(f'Error occurred: {ex}')
            else:
                if response.status_code != 200:
                    print(f'Got error response! statuscode = {response.status_code} response text: {response.text}')
                else:
                    self.books += BooksToScrapeSitePageParser(response.text).parse(self.verbose)

            self.rate_limiter.run()

        print(f'Got {len(self.books)} books')