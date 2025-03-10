                    # Sistema de Gestión de Biblioteca Digital -Darwin Maiza-

# Clase-Libro: Representa un libro en la biblioteca.
                                            # LIBROS
class Libro:
    def __init__(self, titulo, autor, categoria, Cod_barra):
        # Inicializa los atributos del libro: título, autor, categoría y Cod_barra
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.Cod_barra = Cod_barra
    def __repr__(self):
        # Representación que devuelve en cadena del objeto Libro, útil para después en la depuración.
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.Cod_barra}')"

# Clase Usuario: Representa un usuario de la biblioteca.
                                            # USUARIOS
class Usuario:
    def __init__(self, nombre, id_usuario):
        # Inicializa los atributos del usuario: nombre e ID de usuario.
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los libros actualmente prestados por el usuario.

    def __repr__(self):
        # Devuelve una representación en cadena del objeto Usuario.
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"

# Clase Biblioteca: Gestiona los libros y usuarios de la biblioteca.
                                            # Biblioteca
class Biblioteca:
    def __init__(self):
        # Inicializa los atributos de la biblioteca: un diccionario para libros y un conjunto para usuarios.
        self.libros = {}  # Diccionario para almacenar libros, con Cod_barra como clave.
        self.usuarios = set()  # Conjunto para almacenar IDs de usuarios únicos.

    def añadir_libro(self, libro):
        # Añade un libro al diccionario de libros, usando el Cod_barra como clave.
        self.libros[libro.isbn] = libro

    def quitar_libro(self, Cod_barra):
        # Elimina un libro del diccionario de libros, si existe el ISBN.
        if isbn in self.libros:
            del self.libros[Cod_barra]

    def registrar_usuario(self, usuario):
        # Añade el ID de un usuario al conjunto de usuarios.
        self.usuarios.add(usuario.id_usuario)

    def dar_baja_usuario(self, id_usuario):
        # Elimina el ID de un usuario del conjunto de usuarios, si existe.
        self.usuarios.discard(id_usuario)

    def prestar_libro(self, Cod_barra, id_usuario):
        # Presta un libro a un usuario, si el libro y el usuario existen.
        if Cod_barra in self.libros and id_usuario in self.usuarios:
            libro = self.libros[Cod_barra]
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    usuario.libros_prestados.append(libro)
                    return f"Libro '{libro.titulo}' prestado a {usuario.nombre}."
        return "No se puede prestar el libro."

    def devolver_libro(self, isbn, id_usuario):
        # Devuelve un libro prestado por un usuario.
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                if any(libro.isbn == isbn for libro in usuario.libros_prestados):
                    usuario.libros_prestados = [libro for libro in usuario.libros_prestados if libro.isbn != isbn]
                    return f"Libro '{isbn}' devuelto por {usuario.nombre}."
        return "No se puede devolver el libro."

    def buscar_libro(self, criterio, valor):
        # Busca libros por título, autor o categoría.
        resultados = []
        for libro in self.libros.values():
            if (criterio == 'titulo' and libro.titulo == valor) or \
               (criterio == 'autor' and libro.autor == valor) or \
               (criterio == 'categoria' and libro.categoria == valor):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Lista los libros prestados por un usuario específico.
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario.libros_prestados
        return []