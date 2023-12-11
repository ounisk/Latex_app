from pathlib import Path
from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings
from config import ALIST_FILE_PATH, BIB_FILE_PATH

class ReferenceRepository:
    def __init__(self, file_path, bib_file_path):
        self._file_path = file_path
        self._bib_file_path = bib_file_path

    def _check_file(self):
        Path(self._file_path).touch()

    def _get_list(self):
        references = []

        self._check_file()
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
            
                if len(parts) >= 6:
                    bib_ref = parts[0]
                    ref_type = parts[1]
                    author = parts[2]
                    title = parts[3]
                    if ref_type == 'book':
                        year = parts[4]
                        publisher = parts[5]
                        references.append(Book(ref_type, author, title, year, publisher, bib_ref))
                    elif ref_type == 'article':
                        journal = parts[4]
                        year = parts[5]
                        references.append(Article(ref_type, author, title, journal, year, bib_ref))
                    elif ref_type == 'inproceedings':
                        book_title = parts[4]
                        publisher = parts[5]
                        year = parts[6]
                        references.append(InProceedings(ref_type, author, title, book_title,\
                                                        publisher, year, bib_ref))
            return references

    def delete_from_repository(self, bib_ref_del): # korjattu toimivaksi
        references = self.find_all()      #hakee filen nykyisillä tiedoilla
        references_without_deleted_reference = []     
        for ref in references:   #jos ref.bib_ref EI mätsää siihen mitä halutaan poistaa, niin lisää uuteen listaan
            if ref.bib_ref != bib_ref_del:
                #print(row)
                references_without_deleted_reference.append(ref)
        self._update(references_without_deleted_reference)   #....ja lopuksi päivittää tällä uudella listalla,
                                                             # jossa ei nyt mukana sitä mikä haluttiin poistaa.                                   
    def find_all(self):
        return self._get_list()

    def create(self, book):
        references = self.find_all()
        references.append(book)
        self._update(references)
        return book

    def delete_all(self):
        list_references = []
        self._update(list_references)

    def _update(self, references):
        self._check_file()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for ref in references:
                row = ""
                if ref.ref_type == "book":
                    exclusive_fields = [ref.year, ref.publisher]
                elif ref.ref_type == "article":
                    exclusive_fields = [ref.journal, ref.year]
                elif ref.ref_type == "inproceedings":
                    exclusive_fields = [ref.book_title, ref.publisher, ref.year]
                row = ";".join(\
                        [ref.bib_ref, ref.ref_type, ref.author, ref.title]+exclusive_fields)    
                file.write(row+"\n")

    def create_file_in_bib(self, filename):
        full_bibfile_path = Path(self._bib_file_path, filename)

        with open(self._file_path, encoding="utf-8") as file_csv:
            with open(full_bibfile_path, "w") as file_bib:
                for row in file_csv:
                    row = row.replace("\n", "")
                    ref_parts = row.split(";")

                    if len(ref_parts) >= 6:
                        bib_ref = ref_parts[0]
                        ref_type = ref_parts[1]
                        author = ref_parts[2]
                        title = ref_parts[3]
                        if ref_type == "book":
                            year = ref_parts[4]
                            publisher = ref_parts[5]
                            bibtex_ref = \
                                f"@{ref_type}{{{bib_ref},\n"f"  author = {{{author}}},\n" \
                            f"  title =  {{{title}}},\n"\
                            f"  year =  {{{year}}},\n"\
                            f"  publisher =  {{{publisher}}},\n"\
                            f"}}\n"
                        elif ref_type == "article":
                            journal = ref_parts[4]
                            year = ref_parts[5]
                            bibtex_ref = f"@{ref_type}{{{bib_ref},\n"f"  author = {{{author}}},\n" \
                            f"  title =  {{{title}}},\n"\
                            f"  journal =  {{{journal}}},\n"\
                            f"  year =  {{{year}}},\n"\
                            f"}}\n"
                        elif ref_type == "inproceedings":
                            book_title = ref_parts[4]
                            publisher = ref_parts[5]
                            year = ref_parts[6]
                            bibtex_ref = f"@{ref_type}{{{bib_ref},\n"f"  author = {{{author}}},\n" \
                            f"  title =  {{{title}}},\n"\
                            f"  book title =  {{{book_title}}},\n"\
                            f"  publisher =  {{{publisher}}},\n"\
                            f"  year =  {{{year}}},\n"\
                            f"}}\n"
                        file_bib.write(bibtex_ref+"\n")

reference_repository = ReferenceRepository(ALIST_FILE_PATH, BIB_FILE_PATH)
