class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 50)
print(persona1 + persona2)
print(persona1 - persona2)