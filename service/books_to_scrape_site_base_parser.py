from bs4 import BeautifulSoup

class BooksToScrapeSiteBaseParser:

    def __init__(self, content_as_string) -> None:
        self.soup = BeautifulSoup(content_as_string, 'html.parser')

    def parse(self):
        pass