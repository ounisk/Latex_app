from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings
from repositories.reference_repository import (reference_repository as default_reference_repository)


class ReferenceService:
    def __init__(self, reference_repository = default_reference_repository):
        self._reference_repository = reference_repository

    def create_reference(self, ref_type, fields):
        if ref_type == 'book':
            ref = Book(ref_type, *fields)
        elif ref_type == 'article':
            ref = Article(ref_type, *fields)
        elif ref_type == 'inproceedings':
            ref = InProceedings(ref_type, *fields)
        return self._reference_repository.create(ref)

    def print_refs(self):
        return self._reference_repository.find_all()

    def delete_all_references(self):
        self._reference_repository.delete_all()  #tarvitaan etenkin testauksessa tyhjentämään file

    def create_bib_format_file(self, filename):
        bib_file = self._reference_repository.create_file_in_bib(filename)
        return bib_file

# tänne myöhemmin lisää toimintoja....
references_service = ReferenceService()
