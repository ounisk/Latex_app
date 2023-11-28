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
        return f"  Type: {self.ref_type}\n  Author: {self.author}\n  \
            Title: {self.title}\n  Book Title: {self.book_title}\
            \n  Publisher: {self.publisher}\n  Year: {self.year}\n"
