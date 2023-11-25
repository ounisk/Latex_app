from pathlib import Path
from entities.book import Book
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
                #print(row)
                row = row.replace("\n", "")
                parts = row.split(";")
                #print("Osat:")
                #print(parts)
                author = parts[0]
                name = parts[1]
                year = parts[2]
                publisher = parts[3]

                references.append(Book(author, name, year, publisher))

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

                row = f"{ref.author};{ref.name};{ref.year};{ref.publisher}"
                file.write(row+"\n")
             #fileen lisätty tieto tulee str:nä

reference_repository = ReferenceRepository(ALIST_FILE_PATH)
