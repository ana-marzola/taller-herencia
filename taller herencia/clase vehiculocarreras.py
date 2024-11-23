class VehiculoCarreras:
    def _init_(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Máxima: {self.velocidad_maxima} km/h")

class CocheF1(VehiculoCarreras):
    def _init_(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super()._init_(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")

class MotoGP(VehiculoCarreras):
    def _init_(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super()._init_(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Carenado: {self.tipo_carenado}")

# Ejemplo de uso
coche = CocheF1("Ferrari", "SF21", 350, "Lisas")
coche.mostrar_info()

moto = MotoGP("Yamaha", "YZR-M1", 300, "Deportiva")
moto.mostrar_info()