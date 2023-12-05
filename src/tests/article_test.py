import os
import sys
import unittest

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, '..'))

from entities.article import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.article = Article('article', 'Kalle', 'kertomus', 'journal', 2000, 'Kal00')

    def test_right_print(self):
        output = f"      Type: article\n    Author: Kalle\n     Title: kertomus\n   Journal: journal\n      Year: 2000\n   Bib ref: Kal00\n"
        self.assertEqual(str(self.article), output)
