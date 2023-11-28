import unittest
from services.reference_services import ReferenceService
from entities.book import Book, Article, InProceedings
#from repositories.reference_repository import ReferenceRepository


class TestReferenceService(unittest.TestCase): 
    def setUp(self):
        self.reference_service = ReferenceService() #(ReferenceRepository())
        #self.ref_book1 = Book("Waltari", "Sinuhe", "1900", "Otava")


    def test_adding_book_reference_is_on_the_list(self):
        self.reference_service.delete_all_references()
        self.reference_service.create_reference("book", ["Waltari", "Sinuhe", "1900", "Otava", "Wal00"])

        references = self.reference_service.print_refs()
        self.assertEqual((references[0].author, references[0].name, references[0].year, references[0].publisher), ("Waltari", "Sinuhe", "1900", "Otava"))

#Lisää testit "lisää artikkeli", "lisää inproceedings"
