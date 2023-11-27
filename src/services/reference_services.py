from entities.book import Book, Article, InProceedings
from repositories.reference_repository import (reference_repository as default_reference_repository)


class ReferenceService:
    def __init__(self, reference_repository = default_reference_repository):
        self._reference_repository = reference_repository

# käyttöliittymästä kutsu jossa (aut, name, yr, publ.)
    def create_ref_book(self, bib_ref, author, name, year, publisher):
        ref_type = "book"
        book = Book(bib_ref, ref_type, author, name, year, publisher)

        reference = self._reference_repository.create(book)

        return reference

    def create_ref_article(self, bib_ref,  author, title, journal, year):
        ref_type = "article"
        article = Article(bib_ref, ref_type, author, title, journal, year)

        reference = self._reference_repository.create(article)

        return reference
    
    def create_ref_inpro(self,bib_ref, author, title, book_title, publisher, year):
        ref_type = "inproceedings"
        inpro = InProceedings(bib_ref, ref_type, author, title, book_title, publisher, year)

        reference = self._reference_repository.create(inpro)

        return reference

    def print_refs(self):
        ref_list = self._reference_repository.find_all()
        return ref_list

    def delete_all_references(self):
        self._reference_repository.delete_all()  #tarvitaan etenkin testauksessa tyhjentämään file

    def create_bib_format_file(self):
        bib_file = self._reference_repository.create_file_in_bib()
        return bib_file    

# tänne myöhemmin lisää toimintoja....
references_service = ReferenceService()
