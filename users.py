from typing import Protocol
from abc import ABC, abstractmethod
from exceptions import InvalidTitleError

# Protocol defining the interface for a requester
class RequesterProtocol(Protocol):
    def request_book(self, title: str) -> str:
        """Method any requester must apply"""
        ...

# Abstract base class for users
class BaseUser(ABC):
    @abstractmethod
    def request_book(self, title: str) -> str:
        # Abstract method to be implemented by subclasses
        pass

    @abstractmethod
    def test_method(self) -> str:
        # Abstract method to be implemented by subclasses
        pass

# Concrete implementation of a user
class User(BaseUser):
    def __init__(self, name, id):
        # Initialize user with name, id, and an empty list of borrowed books
        self.name = name
        self.id = id
        self.borrowed_books = []

    def request_book(self, title):
        # Simulate a book request
        return f"Book request '{title}' completed"
    
    def test_method(self):
        # Example method to demonstrate usage of abstract base class
        return "This is a test method from User class to know how to use ABC"
    
    @property
    def full_name(self):
        # Return a formatted string with the user's name and id
        return f"Name:{self.name}, id: {self.id}"

# Specialized user class for students
class Student(User):
    def __init__(self, name, id, career):
        # Initialize student with additional career attribute and book limit
        super().__init__(name, id) # inherits attributes from father class
        self.career = career
        self.books_limit = 3
    
    @classmethod
    def create_career_specific_student(cls, name, id):
        career = f"{career}"
        return cls(name, id, career='')

    def request_book(self, title):
        # Validate the book title
        if not title:
            raise InvalidTitleError("Book with title {title} is not valid")
        
        # Check if the student can borrow more books
        if len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(title)
            return f"Book loan: {title} authorized"
        else:
            return f"You cannot borrow more books, limit reached: {self.books_limit}"

class Profesor(User):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.books_limit = None
        
    def request_book(self, title):
        self.borrowed_books.append(title)
        return f"Book requested: {title} authorized"


