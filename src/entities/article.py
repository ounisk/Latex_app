class Article:
    def __init__(self, ref_type:str, author:str, title:str, journal:str, year:int, bib_ref:str):
        self.bib_ref = bib_ref
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        return f"  Type: {self.ref_type}\n  Author: {self.author}\n  Title: {self.title}\
            \n  Journal: {self.journal}\n  Year: {self.year}\n"
