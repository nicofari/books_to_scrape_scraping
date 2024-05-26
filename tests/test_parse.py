import unittest
import os

from domain.book import Book
from service.html_parser import HtmlParser

class TestParse(unittest.TestCase):
    
    def test_parse(self):
        target = HtmlParser()

        curr_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(curr_dir, 'example_page.html')) as file:
            file_content = file.read()

        actual = target.parse(file_content)

        self.assertIsInstance(actual, list)
        self.assertEqual(20, len(actual))
        
        book_0 = actual[0]
        self.assertIsInstance(book_0, Book)
        self.assertEqual("Frankenstein", book_0.title)
        self.assertEqual("Two", book_0.rating)
        self.assertEqual("£38.00", book_0.price)
        self.assertEqual("In stock", book_0.availability)

        book_17 = actual[17]
        self.assertIsInstance(book_17, Book)
        self.assertEqual("A Spy's Devotion (The Regency Spies of London #1)", book_17.title)
        self.assertEqual("Five", book_17.rating)
        self.assertEqual("£16.97", book_17.price)
        self.assertEqual("In stock", book_17.availability)

