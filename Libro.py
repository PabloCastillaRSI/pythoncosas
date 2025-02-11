class Libro:
    def __init__(self, titulo, autor, anio_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.anio_publicacion} (ISBN: {self.isbn})"

    def obtener_info(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio_publicacion": self.anio_publicacion,
            "isbn": self.isbn
        }