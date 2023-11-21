class Book:
    def __init__(self, author:str, name:str, year:int, publisher:str):
        self.author = author
        self.name = name
        self.year = year
        self.publisher = publisher

    def __str__(self):
        return f"Type: Book\nAuthor: {self.author}\nTitle: {self.name}\nPublication date: {self.year}\nPublisher: {self.publisher}\n"
    