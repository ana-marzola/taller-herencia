
# Clase base
class Mascota:
    def _init_(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años, Especie: {self.especie}")

# Clase derivada
class Perro(Mascota):
    def _init_(self, nombre, edad, raza):
        super()._init_(nombre, edad, "Perro")
        self.raza = raza

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")

    def ladrar(self):
        print("Guau, guau")

# Clase derivada
class Gato(Mascota):
    def _init_(self, nombre, edad, color):
        super()._init_(nombre, edad, "Gato")
        self.color = color

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")

    def maullar(self):
        print("Miau")

# Ejemplo de uso
perro1 = Perro("Max", 3, "Labrador")
perro1.mostrar_info()
perro1.ladrar()

gato1 = Gato("Luna", 2, "Negro")
gato1.mostrar_info()
gato1.maullar()