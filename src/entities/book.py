class Book:
    def __init__(self, ref_type:str, author:str, title:str, year:int, publisher:str, bib_ref:str):
        self.bib_ref = bib_ref
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher

    def __str__(self):
        spacing = 10
        ref_type = f"{'Type':>{spacing}}: {self.ref_type}"
        author = f"{'Author':>{spacing}}: {self.author}"
        title = f"{'Title':>{spacing}}: {self.title}"
        publisher = f"{'Publisher':>{spacing}}: {self.publisher}"
        year = f"{'Year':>{spacing}}: {self.year}"
        bib_ref = f"{'Bib ref':>{spacing}}: {self.bib_ref}"
        return "\n".join([ref_type, author, name, publisher, year, bib_ref]) + "\n"
