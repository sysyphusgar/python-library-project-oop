import data
from exceptions import NoAvailableBookError, NoAvailableUserError

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        self.users = []

    def available_books(self):
        return [book.title for libro in self.books if book.available]

    def search_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        raise NoAvailableUserError(f"User with id {id} was not found")
    
    def search_book(self, title):
        for libro in self.books:
            if book.title == title and book.available:
                return libro
        raise NoAvailableBookError(f"The book with title {title} is not available")