import unittest
import tempfile
import os
from repositories.reference_repository import ReferenceRepository
from unittest.mock import patch, mock_open
from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings

class TestReferenceRepository(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repository = ReferenceRepository(self.test_file.name, self.temp_dir.name)

#    def tearDown(self):
#        os.remove(self.test_file.name)
#        self.temp_dir.cleanup()

    def test_check_file(self):
        self.repository._check_file()
        self.assertTrue(os.path.exists(self.test_file.name))

    def test_get_list_empty_file(self):
        references = self.repository._get_list()
        self.assertEqual(len(references), 0)

    def test_create_book(self):
        new_book = Book("book", "Kalle", "Kallen OhTu seikkailut", "2023", "Kallen Omakustanne", "KA23")
        self.repository.create(new_book)

        references = self.repository.find_all()
        self.assertTrue(any(book.author == new_book.author and book.title == new_book.title for book in references))

    def test_create_article(self):
        new_article = Article("article", "Kalle", "Kallen OhTu seikkailut", "Kallen journal", "2023", "KA23")
        self.repository.create(new_article)

        references = self.repository.find_all()
        self.assertTrue(any(article.author == new_article.author and article.title == new_article.title for article in references))

    def test_create_inproceedings(self):
        new_inproceedings = InProceedings("inproceedings", "Kalle", "Kallen OhTu seikkailut", "Kallen OhTu kirja", "Kallen Omakustanne", "2023", "KA23")
        self.repository.create(new_inproceedings)

        references = self.repository.find_all()
        self.assertTrue(any(inproceedings.author == new_inproceedings.author and inproceedings.title == new_inproceedings.title for inproceedings in references))

    def test_create_and_find_all(self):
        reference_data = "KA23;book;Kalle;Kallen OhTu seikkailut;2023;Kallen Omakustanne"
        with open(self.test_file.name, 'w', encoding="utf-8") as file:
            file.write(reference_data)

        references = self.repository.find_all()
        self.assertEqual(len(references), 1)

        reference = references[0]
        self.assertEqual(reference.author, "Kalle")
        self.assertEqual(reference.title, "Kallen OhTu seikkailut")

    def test_delete_all(self):
        book = Book("book", "Kalle", "Kallen OhTu seikkailut", "2023", "Kallen Omakustanne", "KA23")
        self.repository.create(book)

        self.repository.delete_all()

        references = self.repository.find_all()
        self.assertEqual(len(references), 0)

    def test_create_file_in_bib(self):
        book = Book("book", "Kalle", "Kallen OhTu seikkailut", "2023", "Kallen Omakustanne", "KA23")
        self.repository.create(book)

        mock_file = unittest.mock.mock_open()

        with unittest.mock.patch('builtins.open', mock_file):
            self.repository.create_file_in_bib('test_bib_file.bib')

        self.assertEqual(mock_file.call_count, 2)

    def test_create_file_in_bib_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            self.repository.create_file_in_bib('test.bib')
            with open('test.bib', 'r') as bibfile:
                content = bibfile.read()
                self.assertEqual(content, '')
