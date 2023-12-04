import os
import sys
import unittest

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, '..'))

from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('book', 'Kalle', 'kertomus', 2023, 'kustantaja', 'Kal00')

    def test_right_print(self):
        output = f"      Type: book\n    Author: Kalle\n     Title: kertomus\n Publisher: kustantaja\n      Year: 2023\n"
        self.assertEqual(str(self.book), output)
