import os
import sys
import unittest

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, '..'))

from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Kalle', 'kertomus', 2000, 'kustantaja')

    def test_right_print(self):
        output = f"Type: Book\nAuthor: Kalle\nTitle: kertomus\
            \nPublication date: 2000\nPublisher: kustantaja\n"
        self.assertEqual(str(self.book), output)