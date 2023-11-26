from pathlib import Path
from entities.book import Book, Article, InProceedings
from config import ALIST_FILE_PATH



class ReferenceRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        #self._references = []


    def _check_file(self):
        Path(self._file_path).touch()

    def _get_list(self):
        references = []

        self._check_file()
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                if parts[0]== "book": #
                    ref_type = parts[0]   #
                    author = parts[1]
                    name = parts[2]
                    year = parts[3]
                    publisher = parts[4]

                    references.append(Book(ref_type, author, name, year, publisher))

                if parts[0] == "article":
                    ref_type = parts[0]   #
                    author = parts[1]
                    title = parts[2]
                    journal = parts[3]
                    year = parts[4]

                    references.append(Article(ref_type, author, title, journal, year))

                if parts[0] == "inproceedings":
                    ref_type = parts[0]
                    author = parts[1]
                    title = parts[2]
                    book_title = parts[3]
                    publisher = parts[4]
                    year = parts[5]

                    references.append(InProceedings(ref_type, author, title, book_title, publisher, year))
        return references


    def find_all(self):
        #return self._references
        return self._get_list()


    def create(self, book):
        references = self.find_all()
        references.append(book)

        #self._references = references
        self._update(references)   #uuden kirjan jälkeen updatetaan file
        return book


    def delete_all(self):    #tyhjentää koko listan, hyödyksi esim. testaamisessa
        list_references = []
        self._update(list_references)



    def _update(self, references):   #päivitää filen uusilla tiedoilla
        self._check_file()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for ref in references:
                if ref.ref_type == "book":
                    row = f"{ref.ref_type};{ref.author};{ref.name};{ref.year};{ref.publisher}"
                    file.write(row+"\n")
                if ref.ref_type == "article":
                    row = f"{ref.ref_type};{ref.author};{ref.title};{ref.journal};{ref.year}"
                    file.write(row+"\n")
                if ref.ref_type == "inproceedings":
                    row = f"{ref.ref_type};{ref.author};{ref.title};{ref.book_title};{ref.publisher};{ref.year}"
                    file.write(row+"\n")

             #fileen lisätty tieto tulee str:nä

reference_repository = ReferenceRepository(ALIST_FILE_PATH)
