from exceptions import NoAvailableBookError, NoAvailableUserError
from persistence import Persistence

persistence = Persistence()
library = persistence.load_data()

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

persistence.save_data(library)

