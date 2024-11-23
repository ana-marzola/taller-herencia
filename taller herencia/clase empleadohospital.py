class EmpleadoHospital:
    def _init_(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, ID: {self.id}, Departamento: {self.departamento}, Salario: {self.salario_base}")

class Medico(EmpleadoHospital):
    def _init_(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super()._init_(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}, Pacientes: {self.num_pacientes}")

class Enfermero(EmpleadoHospital):
    def _init_(self, nombre, id, departamento, salario_base, turno, planta):
        super()._init_(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Turno: {self.turno}, Planta: {self.planta}")

# Ejemplo de uso
medico1 = Medico("Dr. López", 101, "Cardiología", 5000, "Cardiología", 30)
medico1.mostrar_info()

enfermero1 = Enfermero("Ana Pérez", 201, "Pediatría", 3000, "Noche", 2)
enfermero1.mostrar_info()