class App:
    def __init__(self, reference_services, io):
        self.reference_services = reference_services
        self.io = io
        self.read_ref = {"book": self._read_book, "article": self._read_article
                  , "inproceedings": self._read_inproceedings}

    def run(self):
        self.io.write("Welcome to Latex app")
        while True:
            command = self.io.read(f"Choose command (add, print, create bib):")  # Lisää vaihtoehtoja myöhemmin

            if not command:
                break

            if command == "add":
                ref_type = self.io.read(f"Choose reference type (book, article or inproceedings):")
                
                if ref_type in ["book", "article", "inproceedings"]:
                    fields = self.read_ref[ref_type]()
                    self.reference_services.create_reference(ref_type, fields)
                    self.io.write("Reference added")

            elif command == "print":
                ref_list = self.reference_services.print_refs()
                print("***REFERENCES***")      
                for ref in ref_list:   #siirretty tulostus tänne services:in puolelta
                   print(ref)

            elif command == "create bib":
                self.reference_services.create_bib_format_file()
                print(".bib file has been created")

    def _read_reference(self, fields):
        return [self.io.read(f'Add {field}') for field in fields + ['bib_ref']]

    def _read_book(self):
       return self._read_reference(['author','title','year','publisher'])
    
    def _read_article(self):
        return self._read_reference(['author','title','journal','year'])

    def _read_inproceedings(self):
       return self._read_reference(['author','title','book_title','publisher','year'])



