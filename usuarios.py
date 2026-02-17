from typing import Protocol

class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo} realizada'"

class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula) # hereda atributos de clase padre
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Prestamo del libro: {titulo} autorizado"
        else:
            return f"No puedes prestar mas libros, limite alcanzado: {self.limite_libros}"

    def devolver_libro(self, titulo):
            self.libros_prestados.remove(titulo)
            return f"Libro devuelto: {titulo}"

class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None
        
    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado"
    

