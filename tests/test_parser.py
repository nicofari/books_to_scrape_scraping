import unittest
import os

from domain.book import Book
from service.bts_parser import BooksToScrapeSitePageParser


class TestParse(unittest.TestCase):

    def test_parse(self):
        curr_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(curr_dir, 'books_page.html')) as file:
            file_content = file.read()

        target = BooksToScrapeSitePageParser(file_content)

        actual = target.parse(False)

        self.assertIsInstance(actual, list)
        self.assertEqual(20, len(actual))

        book_0 = actual[0]
        self.assertIsInstance(book_0, Book)
        self.assertEqual("A Light in the Attic", book_0.title)
        self.assertEqual("Three", book_0.rating)
        self.assertEqual("£51.77", book_0.price)
        self.assertEqual("In stock", book_0.availability)

        book_17 = actual[17]
        self.assertIsInstance(book_17, Book)
        self.assertEqual("Mesaerion: The Best Science Fiction Stories 1800-1849", book_17.title)
        self.assertEqual("One", book_17.rating)
        self.assertEqual("£37.59", book_17.price)
        self.assertEqual("In stock", book_17.availability)

        book_7 = actual[7]
        self.assertEqual("The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull", book_7.title)