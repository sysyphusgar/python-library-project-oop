from typing import Protocol

class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Metodo que debe implementar cualquier libro prestado"""
        ...

    def devolver(self) -> str:
        """Metodo que debe implementar cualquier libro prestado"""
        ...
    
    def calcular_duracion(self) -> str:
        """Metodo que debe implementar cualquier libro prestado"""
        ...

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
        return f"{self.titulo} prestado exitosamente. Total prestamos: {self.__veces_prestado}"

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} devuelto y disponible nuevamente."
    
    def es_popular(self):
        return self.__veces_prestado > 5
    
    def get_veces_prestado(self): # getter
        return self.__veces_prestado
    
    def set_veces_prestado(self, veces_prestado):  # setter
        self.__veces_prestado = veces_prestado

    def calcular_duracion(self):
        return "El libro se prestara por 7 dias"

class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"

class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"