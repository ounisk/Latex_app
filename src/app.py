class App:
    def __init__(self, reference_services, io):
        self.reference_services = reference_services
        self.io = io

    def run(self):
        self.io.write("Welcome to Latex app")
        while True:
            command = self.io.read("Choose command (add): ")  # Lisää vaihtoehtoja myöhemmin

            if not command:
                break

            if command == "add":
                ref_type = self.io.read("Choose reference type (book): ")

                if not ref_type:
                    break

                if ref_type == "book":
                    author = self.io.read("Add author: ")
                    name = self.io.read("Add title: ")
                    year = self.io.read("Add publication date: ")
                    publisher = self.io.read("Add publisher: ")

                    self.reference_services.create_ref(author, name, year, publisher)

                    self.io.write("Reference added")
