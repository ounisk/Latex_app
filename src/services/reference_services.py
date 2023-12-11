from datetime import datetime
from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings
from repositories.reference_repository import (reference_repository as default_reference_repository)


class UserInputError(Exception):
    pass

class ReferenceService:
    def __init__(self, reference_repository = default_reference_repository):
        self._reference_repository = reference_repository

    def create_reference(self, ref_type, fields):
        if ref_type == 'book':
            self.validate_year(int(fields[2]))
            ref = Book(ref_type, *fields)

        elif ref_type == 'article':
            self. validate_year(int(fields[3]))
            ref = Article(ref_type, *fields)

        elif ref_type == 'inproceedings':
            self. validate_year(int(fields[4]))
            ref = InProceedings(ref_type, *fields)

        return self._reference_repository.create(ref)

    def print_refs(self):
        return self._reference_repository.find_all()

    def delete_all_references(self):
        self._reference_repository.delete_all()

    def create_bib_format_file(self, filename):
        bib_file = self._reference_repository.create_file_in_bib(filename)
        return bib_file

    def validate_year(self, year):
        current_year = (datetime.now()).year
        if not 0<= year <= current_year:
            raise UserInputError(\
                f"Year has to be in the range of 0-{current_year}. Please try again.")
    
    def delete_reference(self, bib_ref):
        self._reference_repository.delete_from_repository(bib_ref)


references_service = ReferenceService()
