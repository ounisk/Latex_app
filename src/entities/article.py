class Article:
    def __init__(self, ref_type:str, author:str, title:str, journal:str, year:int, bib_ref:str):
        self.bib_ref = bib_ref
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        spacing = 10
        ref_type = f"{'Type':>{spacing}}: {self.ref_type}"
        author = f"{'Author':>{spacing}}: {self.author}"
        title = f"{'Title':>{spacing}}: {self.title}"
        journal = f"{'Journal':>{spacing}}: {self.journal}"
        year = f"{'Year':>{spacing}}: {self.year}"
        return "\n".join([ref_type, author, title, journal, year]) + "\n"
