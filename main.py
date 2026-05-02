from library import Library
from data import students_data, books_data
from exceptions import NoAvailableBookError, NoAvailableUserError
import persistence
from users import Profesor, Student
from books import Book
from persistence import Persistence

library = Library("Personal Library vs2")
profesor1 = Profesor("Erick", "114473484")

library.users = students_data + [profesor1]
library.books = books_data
persistence = Persistence()
persistence.save_data(library)
persistence.load_data()

# # Setter example
# test_book = books_data[1]
# test_book.times_loaned = 6

# result = Library.isbn_validation("46466156")
# print(f"The isbn is valid {result}")

# not_available_book = Book.create_not_available("Test book", "Test author", "Test isbn")
# print("Available book?: ", not_available_book.available)

print("Welcome to my Library")

print("Available books: ")
for book in library.available_books:
    print(book.complete_description)
print()

id = input("Type your id: ")

try:
    user = library.search_user(id)
    print(user.id, user.name)
except NoAvailableUserError as e:
    print("The user you are looking for does not exist")
    print(e)

title = input("Type the title of the book you want to search: ")
try:
    book = library.search_book(title)
    print(f"The book you selected is: {book}")
except NoAvailableBookError as e:
    print("The book you are looking for does not exist")
    print(e)

result = user.request_book(book.title)
print(f"\n{result}")

try:
    result_loan = book.loan()
    print(f"\n{result_loan}")
except NoAvailableBookError as e:
    print("The book is not available for loan")
    print(e)

