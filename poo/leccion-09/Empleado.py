class Empleado:
    def __init__(self, nombre: str, sueldo: int) -> None:
        self._nombre = nombre
        self._sueldo = sueldo
    
    def __str__(self) -> str:
        return f'Empleado: [Nombre: {self._nombre}, Sueldo: {self._sueldo}]'
    
    def mostrar_detalles(self):
        return self.__str__()
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre
    
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo: int):
        self._sueldo = sueldo