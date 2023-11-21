from entities.book import Book


class ReferenceService:
    def __init__(self, reference_repository):
        self._reference_repository = reference_repository

    def create_ref(self, author, name, year, publisher): # käyttöliittymästä kutsu jossa (aut, name, yr, publ.)
        book = Book(author, name, year, publisher)

        reference = self._reference_repository.create(book)

        return reference
    
    # tänne myöhemmin lisää toimintoja....