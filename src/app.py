class App:
    def __init__(self, reference_services, io):
        self.reference_services = reference_services
        self.io = io
        self.space = ""

    def run(self):
        self.io.write("Welcome to Latex app")
        while True:
            command = self.io.read(f"Choose command (add or print): {self.space:30}")  # Lisää vaihtoehtoja myöhemmin

            if not command:
                break

            if command == "add":
                ref_type = self.io.read(f"Choose reference type (book, article or inproceedings): {self.space:5}")

                if not ref_type:
                    break

                if ref_type == "book":
                    (author, title, year, publisher) = self._read_book()
                
                    self.reference_services.create_ref_book(author, title, year, publisher)

                    self.io.write("Reference added")

                elif ref_type == "article":
                    (author, title, journal, year) = self._read_article()

                    self.reference_services.create_ref_article(author, title, journal, year)

                    self.io.write("Reference added")

                elif ref_type == "inproceedings":
                    (author, title, book_title, publisher, year) = self._read_inproceedings()

                    self.reference_services.create_ref_inpro(author, title, book_title, publisher, year)

                    self.io.write("Reference added")

            elif command == "print":
                ref_list = self.reference_services.print_refs()
                print("***VIITTEET***")      
                for ref in ref_list:   #siirretty tulostus tänne services:in puolelta
                   print(ref)


    def _read_book(self):
        author = self.io.read(f"Add author: {self.space:49}")
        title = self.io.read(f"Add title: {self.space:50}")
        year = self.io.read(f"Add publication date: {self.space:39}")
        publisher = self.io.read(f"Add publisher: {self.space:46}")

        return (author, title, year, publisher)
    
    def _read_article(self):
        author = self.io.read(f"Add author: {self.space:49}")
        title = self.io.read(f"Add title: {self.space:50}")
        journal = self.io.read(f"Add journal: {self.space:48}")
        year = self.io.read(f"Add publication date: {self.space:39}")

        return (author, title, journal, year)

    def _read_inproceedings(self):
        author = self.io.read(f"Add author: {self.space:49}")
        title = self.io.read(f"Add title: {self.space:50}")
        book_title = self.io.read(f"Add book title: {self.space:45}")
        publisher = self.io.read(f"Add publisher: {self.space:46}")
        year = self.io.read(f"Add publication date: {self.space:39}")

        return (author, title, book_title, publisher, year)
