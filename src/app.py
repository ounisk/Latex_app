class App:
    def __init__(self, reference_services, io):
        self.reference_services = reference_services
        self.io = io

    def run(self):
        self.io.write("Welcome to Latex app")
        while True:
            command = self.io.read(f"Choose command (add or print):")  # Lisää vaihtoehtoja myöhemmin

            if not command:
                break

            if command == "add":
                ref_type = self.io.read(f"Choose reference type (book, article or inproceedings):")

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

    def _read_reference(self, fields):
        return (self.io.read(f'Add {field}') for field in fields)

    def _read_book(self):
        return self._read_reference(['author','title','year','publisher'])
    
    def _read_article(self):
        return self._read_reference(['author','title','journal','year'])

    def _read_inproceedings(self):
        return self._read_reference(['author','title','book_title','publisher','year'])
