import data
from exceptions import NoAvailableBookError, NoAvailableUserError

class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = []
        self.users = []

    @property
    def available_books(self):
        return [book for book in self.books if book.available]

    def search_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        raise NoAvailableUserError(f"User with id {id} was not found")
    
    def search_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                return book
        raise NoAvailableBookError(f"The book with title {title} is not available")
    
    @staticmethod # does not operate on an instance
    def isbn_validation(isbn):
        return len(isbn) >= 10