class InProceedings:
    def __init__(self, ref_type:str, author:str, title:str, book_title:str,\
                 publisher:str, year:int, bib_ref:str):
        self.bib_ref = bib_ref
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.book_title = book_title
        self.publisher = publisher
        self.year = year

    def __str__(self):
        spacing = 10
        ref_type = f"{'Type':>{spacing}}: {self.ref_type}"
        author = f"{'Author':>{spacing}}: {self.author}"
        title = f"{'Title':>{spacing}}: {self.title}"
        book_title = f"{'Book title':>{spacing}}: {self.book_title}"
        publisher = f"{'Publisher':>{spacing}}: {self.publisher}"
        year = f"{'Year':>{spacing}}: {self.year}"
        return "\n".join([ref_type, author, title, book_title, publisher, year]) + "\n"
