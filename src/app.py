import re
from config import BIB_FILENAME


class App:
    def __init__(self, reference_services, io):
        self.reference_services = reference_services
        self.io = io
        self.read_ref = {"book": self._read_book, "article": self._read_article
                  , "inproceedings": self._read_inproceedings}
    
    # Should this function be in this file? 
    def _is_valid_filename(self, filename):
        return bool(re.match("^[A-Za-z0-9_.]+$", filename))
    
    def run(self):
        self.io.write("\n\nWelcome to Latex app\n")
        # Different ways to choose the reference type, lower case.
        reference_type_map = {'b': 'book', 'book': 'book', 
                              'a': 'article', 'article': 'article', 
                              'i': 'inproceedings', 'inproceedings': 'inproceedings'}
    
        while True:
            command = self.io.read(f"Choose command (A)dd, (P)rint, (C)reate bib:").lower()  # Lisää vaihtoehtoja myöhemmin

            if not command:
                break

            if command in ["a", "add"]:
                ref_type_input = self.io.read(f"Choose reference type (B)ook, (A)rticle or (I)nproceedings):").lower()
                ref_type = reference_type_map.get(ref_type_input)
    
                if ref_type:
                        fields = self.read_ref[ref_type]()
                        self.reference_services.create_reference(ref_type, fields)
                        self.io.write(f"\nReference type {ref_type} added")
                else:
                    self.io.write("Invalid reference type.\n")

            elif command in ["p", "print"]:
                ref_list = self.reference_services.print_refs()
                print("\n\n***REFERENCES***\n")      
                for ref in ref_list:   #siirretty tulostus tänne services:in puolelta
                   print(ref)
                
            elif command in ["c", "create BibTeX file"]:
                while True:
                    default_filename = BIB_FILENAME
                    filename_input = self.io.read(f"Enter filename for BibTeX file (default: {default_filename}):").strip()
                    filename = filename_input if filename_input else BIB_FILENAME
                    
                    if self._is_valid_filename(filename):
                        self.reference_services.create_bib_format_file(filename)
                        self.io.write(f"Your BibTeX file '{filename}' has been created\n")
                        break
                    else:
                        self.io.write("\nInvalid filename. Only letters, numbers, and underscores are allowed.")

    def _read_reference(self, fields):
        print("\n")
        return [self.io.read(f'Add {field}') for field in fields + ['bib_ref']]

    def _read_book(self):
       return self._read_reference(['author','title','year','publisher'])
    
    def _read_article(self):
        return self._read_reference(['author','title','journal','year'])

    def _read_inproceedings(self):
       return self._read_reference(['author','title','book_title','publisher','year'])



