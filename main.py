from biblioteca import Biblioteca
from libros import Libro
from usuarios import Estudiante, Profesor, SolicitanteProtocol

estudiante1 = Estudiante("Juan", "324324234", "Sistemas")
estudiante2 = Estudiante("Felipe", "840394324", "Psicologia")
profesor1 = Profesor("Erick", "114473484")

usuarios: list[SolicitanteProtocol] = [estudiante1, estudiante2, profesor1]

for usuario in usuarios:
    print(usuario.solicitar_libro("Titulo de ejemplo"))


mi_libro_no_disponible = LibroFisico(
    "Alicia en el Pais de las Maravillas",
    "Lewis Carroll",
    "98985435435",
    False
)

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", True)
otro_libro = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-14-310502-9", True)
libro_fisico1 = LibroFisico("La era del capitalismo de la Vigilancia", "Shoshana Zuboff", "46554564")
libro_digital1 = LibroDigital("El Extranjero", "Albert Camus", "5646456465", False)

biblioteca = Biblioteca("Platzi Biblioteca")
biblioteca.libros = [ mi_libro, otro_libro, mi_libro_no_disponible, libro_digital1]
print(biblioteca.libros_disponibles())

