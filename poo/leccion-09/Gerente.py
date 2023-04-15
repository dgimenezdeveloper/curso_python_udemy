from Empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo: int, departamento: str) -> None:
        super().__init__(nombre, sueldo)
        self._departamento = departamento
    
    def __str__(self) -> str:
        return f'Gerente [ Departamento: {self._departamento}] {super().__str__()}'
    
    # def mostrar_detalles(self):
    #     return self.__str__()
    
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento: str):
        self._departamento = departamento