# Clase base
class TransportePublico:
    def _init_(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}, Capacidad: {self.capacidad} pasajeros")

# Clase derivada
class Autobus(TransportePublico):
    def _init_(self, tipo, capacidad, ruta):
        super()._init_(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Ruta: {self.ruta}")

# Clase derivada
class Tren(TransportePublico):
    def _init_(self, tipo, capacidad, numero_vagones):
        super()._init_(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Vagones: {self.numero_vagones}")

# Ejemplo de uso
autobus1 = Autobus("Autobús", 50, "Ruta 25")
autobus1.mostrar_info()

tren1 = Tren("Tren", 200, 10)
tren1.mostrar_info()