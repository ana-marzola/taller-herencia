class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado")

class Cubo(Figura3D):
    def _init_(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

class Esfera(Figura3D):
    def _init_(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

# Ejemplo de uso
cubo = Cubo(3)
print("Volumen del cubo:", cubo.calcular_volumen())

esfera = Esfera(5)
print("Volumen de la esfera:", esfera.calcular_volumen())