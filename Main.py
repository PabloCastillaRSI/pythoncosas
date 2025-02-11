from Libro import Libro
from Bliblioteca import Biblioteca

def main():
    # Crear algunos libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "978-3-16-148410-0")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "978-0-14-243723-0")
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "978-0-15-601219-5")

    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Listar todos los libros en la biblioteca
    print("Libros en la biblioteca:")
    for libro in biblioteca.listar_libros():
        print(libro)

    # Buscar un libro por título
    print("\nBuscando 'El Principito':")
    libros_encontrados = biblioteca.buscar_libro_por_titulo("El Principito")
    for libro in libros_encontrados:
        print(libro)

    # Eliminar un libro por ISBN
    biblioteca.eliminar_libro("978-0-14-243723-0")

    # Listar todos los libros después de eliminar uno
    print("\nLibros en la biblioteca después de eliminar 'Don Quijote de la Mancha':")
    for libro in biblioteca.listar_libros():
        print(libro)

if __name__ == "__main__":
    main()