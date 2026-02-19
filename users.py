from typing import Protocol
from exceptions import LibraryError, InvalidTitleError

class RequesterProtocol(Protocol):
    def request_book(self, title: str) -> str:
        """Method any requester must apply"""
        ...

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def request_book(self, title):
        return f"Book request '{title}' completed"

class Student(User):
    def __init__(self, name, id, career):
        super().__init__(name, id) # inherits attributes from father class
        self.career = career
        self.books_limit = 3

    def request_book(self, title):
        if not title:
            raise InvalidTitleError("Book with title {title} is not valid")
        if len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(title)
            return f"Book loan: {title} authorized"
        else:
            return f"You cannot borrow more books, limit reached: {self.books_limit}"

    def return_book(self, title):
            self.borrowed_books.remove(title)
            return f"Book returned: {title}"

class Profesor(User):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.books_limit = None
        
    def request_book(self, title):
        self.borrowed_books.append(title)
        return f"Book requested: {title} authorized"
    

