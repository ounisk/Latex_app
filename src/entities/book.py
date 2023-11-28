class Book:
    def __init__(self, ref_type:str, author:str, name:str, year:int, publisher:str, bib_ref:str):
        self.bib_ref = bib_ref
        self.ref_type = ref_type
        self.author = author
        self.name = name
        self.year = year
        self.publisher = publisher

    def __str__(self):
        return f"  Type: {self.ref_type}\n  Author: {self.author}\n  Title: {self.name}\
            \n  Publication date: {self.year}\n  Publisher: {self.publisher}\n"
