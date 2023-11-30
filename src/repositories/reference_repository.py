from pathlib import Path
from entities.book import Book
from entities.article import Article
from entities.inpro import InProceedings
from config import ALIST_FILE_PATH, BIB_FILE_PATH

class ReferenceRepository:
    def __init__(self, file_path, bib_file_path):
        self._file_path = file_path
        self._bib_file_path = bib_file_path
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

                if len(parts) >= 6:
                    if parts[1]== "book": #
                        bib_ref = parts[0]
                        ref_type = parts[1]   #
                        author = parts[2]
                        name = parts[3]
                        year = parts[4]
                        publisher = parts[5]

                        references.append(Book(ref_type, author, name, year, publisher, bib_ref))

                    if parts[1] == "article":
                        bib_ref = parts[0]
                        ref_type = parts[1]   #
                        author = parts[2]
                        title = parts[3]
                        journal = parts[4]
                        year = parts[5]

                        references.append(Article(ref_type, author, title, journal, year, bib_ref))

                    if parts[1] == "inproceedings":
                        bib_ref = parts[0]
                        ref_type = parts[1]
                        author = parts[2]
                        title = parts[3]
                        book_title = parts[4]
                        publisher = parts[5]
                        year = parts[6]
                        references.append(InProceedings(ref_type, author, title, book_title,\
                                                        publisher, year, bib_ref))

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
                row = ""
                if ref.ref_type == "book":
                    row = f"{ref.bib_ref};{ref.ref_type};{ref.author};\
                        {ref.name};{ref.year};{ref.publisher}"
                if ref.ref_type == "article":
                    row = f"{ref.bib_ref};{ref.ref_type};{ref.author};\
                        {ref.title};{ref.journal};{ref.year}"
                if ref.ref_type == "inproceedings":
                    row = f"{ref.bib_ref};{ref.ref_type};{ref.author};{ref.title};\
                        {ref.book_title};{ref.publisher};{ref.year}"
                file.write(row+"\n")


    def create_file_in_bib(self):
        with open(self._file_path, encoding="utf-8") as file_csv:   #avataan csv-file

            with open(self._bib_file_path, "w") as file_bib: #avataan bib-file kirjoittamista varten
                for row in file_csv:
                    row = row.replace("\n", "")
                    ref_parts = row.split(";")


                    if len(ref_parts) >= 6:
                        if ref_parts[1]== "book":
                            bib_ref = ref_parts[0]
                            ref_type = ref_parts[1]
                            author = ref_parts[2]
                            title = ref_parts[3]
                            year = ref_parts[4]
                            publisher = ref_parts[5]

                            #bibtex_ref = f"@book{{{bib_ref},\n"f" author = {{{author}}},\n" \
                            bibtex_ref = \
                                f"@{ref_type}{{{bib_ref},\n"f"  author = {{{author}}},\n" \
                            f"  title =  {{{title}}},\n"\
                            f"  year =  {{{year}}},\n"\
                            f"  publisher =  {{{publisher}}},\n"\
                            f"}}\n"

                            file_bib.write(bibtex_ref+"\n")

                        if ref_parts[1]== "article":
                            bib_ref = ref_parts[0]
                            ref_type = ref_parts[1]
                            author = ref_parts[2]
                            title = ref_parts[3]
                            journal = ref_parts[4]
                            year = ref_parts[5]

                            #bibtex_ref = f"@book{{{bib_ref},\n"f" author = {{{author}}},\n" \
                            bibtex_ref = f"@{ref_type}{{{bib_ref},\n"f"  author = {{{author}}},\n" \
                            f"  title =  {{{title}}},\n"\
                            f"  journal =  {{{journal}}},\n"\
                            f"  year =  {{{year}}},\n"\
                            f"}}\n"

                            file_bib.write(bibtex_ref+"\n")

                        if ref_parts[1]== "inproceedings":
                            bib_ref = ref_parts[0]
                            ref_type = ref_parts[1]
                            author = ref_parts[2]
                            title = ref_parts[3]
                            book_title = ref_parts[4]
                            publisher = ref_parts[5]
                            year = ref_parts[6]

                            #bibtex_ref = f"@book{{{bib_ref},\n"f" author = {{{author}}},\n" \
                            bibtex_ref = f"@{ref_type}{{{bib_ref},\n"f"  author = {{{author}}},\n" \
                            f"  title =  {{{title}}},\n"\
                            f"  book title =  {{{book_title}}},\n"\
                            f"  publisher =  {{{publisher}}},\n"\
                            f"  year =  {{{year}}},\n"\
                            f"}}\n"

                            file_bib.write(bibtex_ref+"\n")





reference_repository = ReferenceRepository(ALIST_FILE_PATH, BIB_FILE_PATH)
