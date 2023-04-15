class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

    # Getter --> Permite acceder al método como si fuese un atributo, desde el PP
    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    # Setter --> Permite modificar los atributos de clase

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

#persona2 = Persona('Carla', 'Gomez', 30)
# el _ sugiere no modificar, ni acceder al atributo desde el PP, aunque pueda hacerse. ENCAPSULAMIENTO
#persona2._nombre = 'Sebas'
# NO se puede modificar desde fuera de la clase. ENCAPSULAMIENTO RESTRICTIVO
#persona2.__apellido = 'Daro'


if __name__ == '__main__':
    print(__name__)
