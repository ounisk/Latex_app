import os
import sys
import unittest

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, '..'))

from entities.inpro import InProceedings

class TestInpro(unittest.TestCase):
    def setUp(self):
        self.inpro = InProceedings('inproceedings', 'Kalle', 'kertomus', 'Book', 'Julkaisija', 2000, 'Kal00')

    def test_right_print(self):
        output = f"      Type: inproceedings\n    Author: Kalle\n     Title: kertomus\nBook title: Book\n Publisher: Julkaisija\n      Year: 2000\n"
        self.assertEqual(str(self.inpro), output)
