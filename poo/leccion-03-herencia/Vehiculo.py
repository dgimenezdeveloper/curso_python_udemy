class Vehiculo:
    def __init__(self, color: str, ruedas: int):
        self.__color = color
        self.__ruedas = ruedas
    
    def __str__(self):
        return f'Vehiculo [Color: {self.__color}, Ruedas: {self.__ruedas}]'
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
        
    @property
    def ruedas(self):
        return self.__ruedas
    
    @color.setter
    def ruedas(self, ruedas):
        self.__ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: int):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    
    def __str__(self):
        return f'{super().__str__()} - Coche [Velocidad: {self._velocidad} km/h]'
    
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad: int):
        self._velocidad = velocidad
    
class Bicicleta(Vehiculo):
    def __init__(self, color: str, ruedas: int, tipo: str):
        super().__init__(color, ruedas)
        self._tipo = tipo
    
    def __str__(self):
        return f'{super().__str__()} - Bicicleta: [Tipo: {self._tipo}]'
    
    @property
    def bicicleta_tipo(self):
        return self._tipo
    
    @bicicleta_tipo.setter
    def bicicleta_tipo(self, tipo: str):
        self._tipo = tipo
