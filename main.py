from service.bts_scraper import BooksToScrapeScraper

def main():

    scraper = BooksToScrapeScraper()
    scraper.scrape()

if __name__ == '__main__':
    main()