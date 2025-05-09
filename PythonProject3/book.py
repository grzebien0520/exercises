#cwiczenie 2
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def set_title(self, title):
        self.title = title
        return title
    def set_author(self, author):
        self.author = author
        return author
    def set_year(self, year):
        self.year = year
        return year
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_year(self):
        return self.year
