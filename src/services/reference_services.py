from entities.book import Book, Article, InProceedings
from repositories.reference_repository import (reference_repository as default_reference_repository)


class ReferenceService:
    def __init__(self, reference_repository = default_reference_repository):
        self._reference_repository = reference_repository

    def create_reference(self, type, fields):
        if type == 'book':
            ref = Book(type, *fields)
        elif type == 'article':
            ref = Article(type, *fields)
        elif type == 'inproceedings':
            ref = InProceedings(type, *fields)
        return self._reference_repository.create(ref)

    def print_refs(self):
        return self._reference_repository.find_all()

    def delete_all_references(self):
        self._reference_repository.delete_all()  #tarvitaan etenkin testauksessa tyhjentämään file

    def create_bib_format_file(self):
        bib_file = self._reference_repository.create_file_in_bib()
        return bib_file    

# tänne myöhemmin lisää toimintoja....
references_service = ReferenceService()
