class Book:
    def __init__(self, ref_type:str, author:str, name:str, year:int, publisher:str):
        self.ref_type = ref_type
        self.author = author
        self.name = name
        self.year = year
        self.publisher = publisher

    def __str__(self):
        return f"  Type: {self.ref_type}\n  Author: {self.author}\n  Title: {self.name}\
            \n  Publication date: {self.year}\n  Publisher: {self.publisher}\n"


class Article:
    def __init__(self, ref_type:str, author:str, title:str, journal:str, year:int):
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        return f"  Type: {self.ref_type}\n  Author: {self.author}\n  Title: {self.title}\
            \n  Journal: {self.journal}\n  Year: {self.year}\n"

class InProceedings:
    def __init__(self, ref_type:str, author:str, title:str, book_title:str, publisher:str, year:int):
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.book_title = book_title
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"  Type: {self.ref_type}\n  Author: {self.author}\n  Title: {self.title}\n  Book Title: {self.book_title}\
            \n  Publisher: {self.publisher}\n  Year: {self.year}\n"
    