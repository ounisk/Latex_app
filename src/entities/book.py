class Book:
    def __init__(self, ref_type:str, author:str, name:str, year:int, publisher:str, bib_ref:str):
        self.bib_ref = bib_ref
        self.ref_type = ref_type
        self.author = author
        self.name = name
        self.year = year
        self.publisher = publisher

    def __str__(self):
        spacing = 10
        ref_type = f"{'Type':>{spacing}}: {self.ref_type}"
        author = f"{'Author':>{spacing}}: {self.author}"
        name = f"{'Title':>{spacing}}: {self.name}"
        publisher = f"{'Publisher':>{spacing}}: {self.publisher}"
        year = f"{'Year':>{spacing}}: {self.year}"
        return "\n".join([ref_type, author, name, publisher, year]) + "\n"
