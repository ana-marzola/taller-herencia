
# Clase base
class MaterialBiblioteca:
    def _init_(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"{self.titulo} ha sido devuelto.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Disponible: {self.disponible}")

# Clase derivada
class Libro(MaterialBiblioteca):
    def _init_(self, titulo, autor, codigo, numero_paginas, genero):
        super()._init_(titulo, autor, codigo)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Páginas: {self.numero_paginas}, Género: {self.genero}")

# Clase derivada
class Revista(MaterialBiblioteca):
    def _init_(self, titulo, autor, codigo, numero_edicion, fecha_publicacion):
        super()._init_(titulo, autor, codigo)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Edición: {self.numero_edicion}, Publicación: {self.fecha_publicacion}")

# Ejemplo de uso
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "L001", 96, "Ficción")
libro1.mostrar_info()
libro1.prestar()
libro1.devolver()

revista1 = Revista("National Geographic", "Varios", "R001", 155, "2024-01")
revista1.mostrar_info()