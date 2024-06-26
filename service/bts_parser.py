from bs4 import BeautifulSoup
from domain.book import Book
from service.parse_exception import ParseException


class BooksToScrapeSiteBaseParser:

    def __init__(self, content_as_string) -> None:
        self.soup = BeautifulSoup(content_as_string, 'html.parser')

    def parse(self, verbose):
        pass


class BooksToScrapeSitePageParser(BooksToScrapeSiteBaseParser):

    def parse(self, verbose):
        soup = self.soup

        ret = []

        for article in soup.select('article.product_pod'):
            a_inside_h3 = article.select('h3>a')
            if a_inside_h3 is None or a_inside_h3[0] is None:
                raise ParseException("Parse failed: unable to find book's title")
            title = a_inside_h3[0]['title']

            p_rating = article.select('p.star-rating')
            if p_rating is None or p_rating[0]['class'][1] is None:
                raise ParseException("Parse failed: unable to find book's rating")
            rating = p_rating[0]['class'][1]

            p_price = article.select('p.price_color')
            if p_price is None or p_price[0] is None:
                raise ParseException("Parse failed: unable to find book's price")
            price = p_price[0].text

            p_availability = article.select('p.instock')
            if p_availability is None:
                raise ParseException("Parse failed: unable to find book's availability")

            availability = p_availability[0].text.strip()

            if verbose:
                print(f'Got {title} {rating} {price} {availability}')

            ret.append(Book(title, rating, price, availability))

        return ret


class BooksToScrapeSiteSingleParser(BooksToScrapeSiteBaseParser):

    def parse():
        pass
