class Persona:
    contador_personas = 0
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    def __init__(self, nombre: str, edad: int):
        self.__id_persona = Persona.generar_siguiente_valor()
        self._nombre = nombre
        self._edad = edad
    
    def __str__(self) -> str:
        return f'Persona [ID: {self.__id_persona} - NOMBRE: {self._nombre} - EDAD: {self._edad}]'

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad: int):
        self._edad = edad

persona1 = Persona('Juan', 28)
persona2 = Persona('Daro', 36)
print(persona1)
print(persona2)