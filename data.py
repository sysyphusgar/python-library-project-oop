from books import Book, PhysicalBook
from users import Student

# Books creation
book1 = PhysicalBook("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
book2 = PhysicalBook("Alicia en el Pais de las Maravillas", "Lewis Carroll", "98985435435")
book3 = Book("El Principito", "Antoine de Saint-Exupéry", "978-0-14-310502-9")
book4 = Book("Don Quijote de la Mancha", "Miguel de Cervantes", "978-0-14-243723-0")
book5 = Book("La Sombra del Viento", "Carlos Ruiz Zafón", "978-0-14-303490-2")
book6 = Book("El Alquimista", "Paulo Coelho", "978-0-06-112241-5")
book7 = Book("1984", "George Orwell", "978-0-452-28423-4")
book8 = Book("El Gran Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
book9 = Book("Matar a un Ruiseñor", "Harper Lee", "978-0-06-112008-4")
book10 = Book("El Código Da Vinci", "Dan Brown", "978-0-385-50420-8")

# Students creation
student1 = Student("Juan", "324324234", "Sistemas")
student2 = Student("Felipe", "840394324", "Psicologia")
student3 = Student("Maria", "123456789", "Derecho")
student4 = Student("Ana", "987654321", "Medicina")
student5 = Student("Luis", "555555555", "Arquitectura")
student6 = Student("Sofia", "111111111", "Economia")
student7 = Student("Carlos", "222222222", "Ingenieria")
student8 = Student("Laura", "333333333", "Psicologia")
student9 = Student("Diego", "444444444", "Sistemas")
student10 = Student("Valentina", "666666666", "Derecho")

books_data = [
    book1,
    book2,
    book3,
    book4,
    book5,
    book6,
    book7,
    book8,
    book9,
    book10,
]
students_data = [
    student1,
    student2,
    student3,
    student4,
    student5,
    student6,
    student7,
    student8,
    student9,
    student10,
]
