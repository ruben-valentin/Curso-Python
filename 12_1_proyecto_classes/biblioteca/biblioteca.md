# Sistema de Biblioteca en Python

Este proyecto implementa un sistema básico de biblioteca en Python, dividido en varios archivos para mejorar la modularidad y la organización.

---

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```bash
biblioteca/
├── main.py         # Archivo principal para ejecutar el programa
├── book.py         # Clase Book (representa un libro)
├── library.py      # Clase Library (representa la biblioteca)
```

---

## Contenido de los Archivos

### `book.py`

Este archivo contiene la definición de la clase `Book`, que representa cada libro. Incluye métodos para gestionar el estado del libro (prestado o disponible).

```python
class Book:
    def __init__(self, title, author):
        """
        Constructor de la clase Book.
        :param title: Título del libro.
        :param author: Autor del libro.
        """
        self.title = title  # Propiedad pública: título del libro
        self.author = author  # Propiedad pública: autor del libro
        self.__is_borrowed = False  # Propiedad privada: indica si el libro está prestado

    def borrow(self):
        """
        Método para prestar el libro.
        Retorna True si se prestó exitosamente, False si ya está prestado.
        """
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def return_book(self):
        """
        Método para devolver el libro.
        """
        self.__is_borrowed = False

    def is_borrowed(self):
        """
        Método para verificar si el libro está prestado.
        """
        return self.__is_borrowed

    def __str__(self):
        """
        Representación en string del libro.
        """
        status = "Prestado" if self.__is_borrowed else "Disponible"
        return f"'{self.title}' por {self.author} ({status})"
```

---

### `library.py`

Este archivo contiene la clase `Library`, que gestiona la lista de libros en la biblioteca. Proporciona métodos para agregar libros, prestar libros, devolver libros y mostrar la lista de libros.

```python
from book import Book  # Importamos la clase Book para manejar libros

class Library:
    def __init__(self):
        """
        Constructor de la clase Library.
        Inicializa una lista vacía de libros.
        """
        self.books = []  # Lista pública para almacenar los libros

    def add_book(self, book):
        """
        Método para agregar un libro a la biblioteca.
        :param book: Instancia de la clase Book.
        """
        self.books.append(book)
        print(f"Libro '{book.title}' agregado a la biblioteca.")

    def show_books(self):
        """
        Método para mostrar los libros disponibles en la biblioteca.
        """
        if not self.books:
            print("La biblioteca está vacía.")
            return
        print("\nLibros en la biblioteca:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def borrow_book(self, title):
        """
        Método para prestar un libro.
        :param title: Título del libro a prestar.
        """
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Has prestado el libro: '{title}'.")
                    return
                else:
                    print(f"El libro '{title}' ya está prestado.")
                    return
        print(f"No se encontró el libro con título: '{title}'.")

    def return_book(self, title):
        """
        Método para devolver un libro.
        :param title: Título del libro a devolver.
        """
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Has devuelto el libro: '{title}'.")
                return
        print(f"No se encontró el libro con título: '{title}'.")
```

---

### `main.py`

Este es el archivo principal donde se inicializa el programa. Utiliza las clases `Book` y `Library` para realizar operaciones específicas como agregar libros, prestar, devolver, y mostrar libros.

```python
from library import Library  # Importamos la clase Library
from book import Book  # Importamos la clase Book

def main():
    # Crear una instancia de la biblioteca
    my_library = Library()

    # Agregar libros a la biblioteca
    book1 = Book("Cien Años de Soledad", "Gabriel García Márquez")
    book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
    book3 = Book("El Principito", "Antoine de Saint-Exupéry")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Mostrar libros
    my_library.show_books()

    # Prestar un libro
    my_library.borrow_book("El Principito")

    # Intentar prestar un libro que ya está prestado
    my_library.borrow_book("El Principito")

    # Devolver un libro
    my_library.return_book("El Principito")

    # Mostrar libros nuevamente
    my_library.show_books()

if __name__ == "__main__":
    main()
```

Este fragmento:

```python
if __name__ == "__main__":
    main()
```

es una construcción común en Python que asegura que el código dentro de este bloque solo se ejecutará cuando el archivo se ejecute directamente, y **no cuando se importe como un módulo** en otro archivo. Si otro archivo importa `main.py`, el código dentro de `main()` no se ejecutará automáticamente a menos que se llame a la función `main()` de forma explícita.

Esto es útil para:

1. **Separar la lógica de ejecución del código** de la definición de funciones o clases.
2. **Permitir la reutilización de funciones y clases** sin ejecutar el código principal cuando se importe el archivo.

---

## Cómo ejecutar el proyecto

Sigue estos pasos para ejecutar el proyecto:

1. Asegúrate de que todos los archivos (`main.py`, `book.py`, `library.py`) estén en la misma carpeta.
2. Abre la terminal en la carpeta donde están los archivos.
3. Ejecuta el programa principal con:

```bash
python main.py
```

---

## Explicación

### `book.py`
- Contiene la definición de la clase `Book` que representa cada libro.
- Proporciona métodos para gestionar el estado del libro (prestado o disponible).

### `library.py`
- Contiene la clase `Library` que gestiona la lista de libros en la biblioteca.
- Incluye métodos para agregar libros, prestar libros, devolver libros y mostrar la lista de libros.

### `main.py`
- Es el archivo principal donde se inicializa el programa.
- Utiliza las clases `Book` y `Library` para realizar operaciones específicas como agregar libros, prestar, devolver, y mostrar libros.

---

## Ventajas de dividir en archivos

1. **Modularidad**: Cada archivo tiene una responsabilidad específica.
2. **Reusabilidad**: Puedes reutilizar las clases `Book` y `Library` en otros proyectos.
3. **Mantenimiento**: Es más fácil actualizar o corregir errores en clases individuales sin afectar todo el proyecto.

---

