import unittest
from unittest.mock import Mock
from datetime import datetime
from services.reference_services import ReferenceService, UserInputError
from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.mock_reference_repository = Mock()
        self.reference_service = ReferenceService(self.mock_reference_repository)

    def test_create_reference_book(self):
        fields = ['Author Name', 'Book Title', '2023', 'Publisher Name', '']
        self.reference_service.create_reference('book', fields)

        self.mock_reference_repository.create.assert_called_once()
        new_ref = self.mock_reference_repository.create.call_args[0][0]
        self.assertIsInstance(new_ref, Book)
        self.assertEqual(new_ref.author, 'Author Name')

    def test_create_reference_article(self):
        fields = ['Author Name', 'Article Title', 'Journal', '2023', '']
        self.reference_service.create_reference('article', fields)

        self.mock_reference_repository.create.assert_called_once()
        new_ref = self.mock_reference_repository.create.call_args[0][0]
        self.assertIsInstance(new_ref, Article)
        self.assertEqual(new_ref.author, 'Author Name')

    def test_create_reference_inproceedings(self):
        fields = ['Author Name', 'Title', 'Book Title', 'Publisher Name', '2023', '']
        self.reference_service.create_reference('inproceedings', fields)

        self.mock_reference_repository.create.assert_called_once()
        new_ref = self.mock_reference_repository.create.call_args[0][0]
        self.assertIsInstance(new_ref, InProceedings)
        self.assertEqual(new_ref.author, 'Author Name')

    def test_delete_reference(self):
        fields1 = ['Author1', 'Book1', '2023', 'Publisher1 Name', 'Au23']
        fields2 = ['Author2', 'Book2', '2020', 'Publisher2 Name', 'Au20']
        self.reference_service.create_reference('book', fields1)
        self.reference_service.create_reference('book', fields2)
        self.assertEqual(self.mock_reference_repository.create.call_count, 2)
        self.reference_service.delete_reference('Au23')
        self.mock_reference_repository.delete_from_repository.assert_called_once_with('Au23')

    def test_validate_year(self):
        with self.assertRaises(UserInputError) as context:
            self.reference_service.validate_year("-1")
        output = "Year has to be in the range of 0-2023. Please try again."
        self.assertEqual(str(context.exception), output)  

    def test_validate_valid_years(self):
        years = [1, 2023, 1900, 2000]
        for year in years:
            self.assertTrue(self.reference_service.validate_year(str(year)))

    def test_validate_non_numeric_years(self):
        years = ["OhTu", "123xyz", "!@#", " 1500", "{}[]"]
        for year in years:
            with self.assertRaises(UserInputError) as test:
                self.reference_service.validate_year(year)
            output = "Year has to be numeric."
            self.assertEqual(str(test.exception), output)

    def test_validate_years_outside_range(self):
        years = [-1, 2123, -1000, 3000]
        current_year = (datetime.now()).year
        for year in years:
            with self.assertRaises(UserInputError) as test:
                self.reference_service.validate_year(str(year))
            output = f"Year has to be in the range of 0-{current_year}. Please try again."
            self.assertEqual(str(test.exception), output)

    def test_create_bib_format_file(self):
        filename = "test.bib"
        self.mock_reference_repository.create_file_in_bib.return_value = True
        result = self.reference_service.create_bib_format_file(filename)
        self.assertEqual(result, True)
        self.mock_reference_repository.create_file_in_bib.assert_called_once_with(filename)

    def test_print_refs_empty(self):
        self.mock_reference_repository.find_all.return_value = []
        result = self.reference_service.print_refs()
        self.assertEqual(result, [])
        self.mock_reference_repository.find_all.assert_called_once()

    def test_print_refs(self):
        reference1 = Book("book", "Author1", "Book1", "2023", "Publisher", "AU23")
        reference2 = Article("article", "Author2", "Article", "Journal", "2023", "A223")
        self.mock_reference_repository.find_all.return_value = [reference1, reference2]
        self.reference_service.print_refs()
        self.mock_reference_repository.find_all.assert_called_once()