class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def aplicar_aumento(self, aumento):
        self.salario += aumento

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario, lenguaje):
        super().__init__(nombre, apellido, salario)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        return f"{self.obtener_nombre_completo()} - Lenguaje: {self.lenguaje} - Salario: {self.salario}"

# Crear empleados
empleado1 = Empleado("Juan", "Pérez", 50000)
empleado2 = Desarrollador("María", "González", 60000, "Python")

# Mostrar información de los empleados
print(empleado1.obtener_nombre_completo())  # Salida: Juan Pérez
print(empleado2.mostrar_info())  # Salida: María González - Lenguaje: Python - Salario: 60000

# Aplicar aumentos
empleado1.aplicar_aumento(5000)
empleado2.aplicar_aumento(7000)

# Mostrar nuevos salarios
print(empleado1.salario)  # Salida: 55000
print(empleado2.salario)  # Salida: 67000
