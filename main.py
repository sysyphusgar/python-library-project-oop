class Libro:  
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0 # el doble __ hace que la variable sea privada (encapsulacion), y mantenga integridad de datos

    def __str__(self):
        return f"{self.titulo} por {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"{self.titulo} prestado exitosamente. Total prestamos: {self.__veces_prestado}"
        return f"{self.titulo} no esta disponible"

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} devuelto y disponible nuevamente."
    
    def es_popular(self):
        return self.__veces_prestado > 5
    
    def get_veces_prestado(self): # getter
        return self.__veces_prestado
    
    def set_veces_prestado(self, veces_prestado):  # setter
        self.__veces_prestado = veces_prestado


mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", True)
otro_libro = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-14-310502-9", True)

otro_libro.set_veces_prestado(10) # modifica valores de veces prestado de manera adecuada, manteniendo integridad de datos

print(otro_libro.get_veces_prestado())

for i in range(6):
    otro_libro.prestar()
    otro_libro.devolver()

print(otro_libro.prestar())


# print(f"mi_libro: {mi_libro.titulo} por {mi_libro.autor}")
# print(f"otro_libro: {otro_libro.titulo} por {otro_libro.autor}")

catalogo = [mi_libro, otro_libro]

for i in catalogo:
    print(i)