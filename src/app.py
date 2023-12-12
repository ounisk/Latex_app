import re
from config import BIB_FILENAME

class App:
    def __init__(self, reference_services, io):
        self.reference_services = reference_services
        self.io = io
        self.read_ref = {"book": self._read_book, "article": self._read_article
                  , "inproceedings": self._read_inproceedings}

    def _is_valid_filename(self, filename):
        return bool(re.match("^[A-Za-z0-9_.]+$", filename))
    
    def summary(self):
        ref_list = self.reference_services.print_refs()
        self.io.write("\nReference Summary\n")
        max_ref_type = max(max([len(ref.ref_type) for ref in ref_list]) + 2,10)
        max_ref_title = max(max([len(ref.title) for ref in ref_list]) + 2,10)
        max_ref_author = max(max([len(ref.author) for ref in ref_list]) + 2,10)
        max_ref_bib = max(max([len(ref.bib_ref) for ref in ref_list]) + 2,10)
        max_ref_year = max(max([len(str(ref.year)) for ref in ref_list]) + 2,10)
        self.io.write(f"{'Type':{max_ref_type}}{'Title':{max_ref_title}}{'Author':{max_ref_author}}{'Bib-ref':{max_ref_bib}}Year\n")
        for ref in ref_list:
            self.io.write(f"{ref.ref_type:{max_ref_type}}{ref.title:{max_ref_title}}{ref.author:{max_ref_author}}{ref.bib_ref:{max_ref_bib}}{ref.year}")          
        self.io.write('\n')
    
    def delete(self):
        self.summary()
        delete_bib_ref = self.io.read(f'Give bibref you want to delete: ').strip()
        self.reference_services.delete_reference(delete_bib_ref)
    
    def run(self):
        self.io.write("\n\nWelcome to Latex app\n")
        
        reference_type_map = {'b': 'book', 'book': 'book', 
                              'a': 'article', 'article': 'article', 
                              'i': 'inproceedings', 'inproceedings': 'inproceedings'}

        while True:
            command = self.io.read(f"Choose command (A)dd, (P)rint, (C)reate bib, (S)ummary, (Q)uit, (D)elete:").lower()  # Lisää vaihtoehtoja myöhemmin

            if command in ["q", "quit"] or not command:
                break

            if command in ["a", "add"]:
                ref_type_input = self.io.read(f"Choose reference type (B)ook, (A)rticle or (I)nproceedings):").lower()
                ref_type = reference_type_map.get(ref_type_input)
    
                if ref_type:
                        fields = self.read_ref[ref_type]()
                        default_bibref = self._add_bibref(ref_type, fields)
                        bibref_input = self.io.read(f"Add bibref for the reference (default: {default_bibref}):").strip()
                        if not bibref_input:
                            bibref_input = default_bibref
                        fields.append(bibref_input)
                        try:
                            self.reference_services.create_reference(ref_type, fields)
                            self.io.write(f"\nReference type {ref_type} added")
                        except Exception as error:
                            self.io.write(str(error))
                            print("\n")
                else:
                    self.io.write("Invalid reference type.\n")
            
            elif command in ['d', 'delete']:
                self.delete()
                self.io.write(f"The reference has been deleted. Select (C)reate bib to update your bib-file.\n")

            elif command in ["p", "print"]:
                ref_list = self.reference_services.print_refs()
                self.io.write("\n\n***REFERENCES***\n")      
                for ref in ref_list:
                   #print(ref)
                   self.io.write(ref)

            elif command in ["s", "summary"]:
                self.summary()
                
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
        return [self.io.read(f'Add {field}') for field in fields]
    
    def _read_book(self):
       return self._read_reference(['author','title','year','publisher'])
    
    def _read_article(self):
        return self._read_reference(['author','title','journal','year'])
    
    def _read_inproceedings(self):
       return self._read_reference(['author','title','book title','publisher','year'])

    def _add_bibref(self, ref_type, fields):
        if ref_type == 'book':
            exclusive_field = fields[2]
        elif ref_type == 'article':
            exclusive_field = fields[3]
        elif ref_type == 'inproceedings':
            exclusive_field = fields[4]
        return f"{fields[0][:2]+exclusive_field[-2:]}"




