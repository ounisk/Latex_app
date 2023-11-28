import os
import sys
import unittest

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, '..'))

from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('book', 'Kalle', 'kertomus', 2000, 'kustantaja', 'Kal00')

    def test_right_print(self):
        output = f"  Type: book\n  Author: Kalle\n  Title: kertomus\
            \n  Publication date: 2000\n  Publisher: kustantaja\n"
        self.assertEqual(str(self.book), output)
