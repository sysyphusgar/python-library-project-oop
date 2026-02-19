from library import Library
from data import students_data, books_data
from exceptions import NoAvailableBookError, NoAvailableUserError
from users import Profesor

library = Library("Personal Library")
profesor1 = Profesor("Erick", "114473484")

library.users = students_data + [profesor1]
library.books = books_data

print("Welcome to my Library")

print("Available books: ")
for title in library.available_books():
    print(f"  - {title}")
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
