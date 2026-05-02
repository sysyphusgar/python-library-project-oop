import json
from datetime import datetime

from books import PhysicalBook
from library import Library

class Persistence:
    def __init__(self, file="library.json") -> None:
        self.file = file

    def save_data(self, library):
        data = {
            "name": library.name,
            "users": [user.__dict__ for user in library.users],
            "books": [book.__dict__ for book in library.books],
            "date_saved": datetime.now().isoformat()
        }

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print("Data:", data["books"][0])
        # Data: {'title': 'Cien Años de Soledad', 'author': 'Gabriel García Márquez', 
        # 'isbn': '978-3-16-148410-0', 'available': True, '_Book__times_loaned': 0}

        library = Library(data["name"])
        for data_book in data["books"]:

            PhysicalBook(
                title=data_book['title'],
                author=data_book['author'],
                isbn=data_book["isbn"],
                available=data_book["available"]
            )
            library.books.append(book)