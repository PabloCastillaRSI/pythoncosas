from Libro import Libro


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
        else:
            raise ValueError("El objeto debe ser una instancia de la clase Libro")

    def eliminar_libro(self, isbn):
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]

    def buscar_libro_por_titulo(self, titulo):
        return [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]

    def listar_libros(self):
        return [str(libro) for libro in self.libros]