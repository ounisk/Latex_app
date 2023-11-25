from entities.book import Book
from repositories.reference_repository import (reference_repository as default_reference_repository)


class ReferenceService:
    def __init__(self, reference_repository = default_reference_repository):
        self._reference_repository = reference_repository

# käyttöliittymästä kutsu jossa (aut, name, yr, publ.)
    def create_ref(self, author, name, year, publisher):
        book = Book(author, name, year, publisher)

        reference = self._reference_repository.create(book)

        return reference


    def print_refs(self):
        ref_list = self._reference_repository.find_all()
        return ref_list   # esim. näin
    


    def delete_all_references(self):
        self._reference_repository.delete_all()  #tarvitaan etenkin testauksessa tyhjentämään file

# tänne myöhemmin lisää toimintoja....



references_service = ReferenceService()

    
