from typing import Protocol
from abc import ABC, abstractmethod
from exceptions import NoAvailableBookError

class BookProtocol(Protocol):
    def loan(self) -> str:
        """Method that any loaned book must implement"""
        ...

    def return_book(self) -> str:
        """Method that any returned book must implement"""
        ...
    
    def calculate_duration(self) -> str:
        """Method that any book must implement to calculate duration"""
        ...

class BaseBook(ABC):
    @abstractmethod
    def calculate_duration(self) -> str:
        pass

class Book(BaseBook):  
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.__times_loaned = 0 # double __ makes a private variable (incapsulation), and keep data integrity

    @classmethod # it is a constructor method
    def create_not_available(cls, title, author, isbn):
        return cls(title, author, isbn, available=False)
        
    def __str__(self):
        return f"{self.title} por {self.author}, ISBN: {self.isbn}, Available: {self.available}"

    def loan(self):
        if not self.available:
            raise NoAvailableBookError(f"Book {self.title} is not available")
        self.__times_loaned += 1
        return f"{self.title} loaned successfully. Total loans: {self.__times_loaned}"

    def return_book(self):
        self.available = True
        return f"{self.title} returned and available again."
    
    @property
    def is_popular(self):
        return self.__times_loaned > 5
    
    @property
    def times_loaned(self): # getter
        return self.__times_loaned
    
    @times_loaned.setter
    def times_loaned(self, times_loaned):  # setter
        if times_loaned > 0:
            self.__times_loaned = times_loaned
        else:
            raise ValueError("The times_loaned value must be higher than 0")
    
    @property
    def complete_description(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def calculate_duration(self) -> str:
        return "The book is loaned for 7 days"

class PhysicalBook(Book):
    def calculate_duration(self):
        return "7 days"

class DigitalBook(Book):
    def calculate_duration(self):
        return "14 days"