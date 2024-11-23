# Clase base
class ProductoElectronico:
    def _init_(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Marca: {self.marca}")

# Clase derivada
class TelefonoMovil(ProductoElectronico):
    def _init_(self, nombre, precio, marca, capacidad_bateria):
        super()._init_(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de Batería: {self.capacidad_bateria} mAh")

# Clase derivada
class Laptop(ProductoElectronico):
    def _init_(self, nombre, precio, marca, tamano_pantalla):
        super()._init_(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño de Pantalla: {self.tamano_pantalla} pulgadas")

# Ejemplo de uso
telefono1 = TelefonoMovil("iPhone 13", 999, "Apple", 3095)
telefono1.mostrar_info()

laptop1 = Laptop("MacBook Pro", 1999, "Apple", 16)
laptop1.mostrar_info()