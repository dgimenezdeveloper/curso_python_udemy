class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia: str):
        self._variable_instancia = variable_instancia

    @property
    def variable_instancia(self):
        return self._variable_instancia

    @variable_instancia.setter
    def variable_instancia(self, variable_instancia):
        self._variable_instancia = variable_instancia

    def __str__(self) -> str:
        return f'Variable de clase: {self.variable_clase} --- Variable Instancia: {self._variable_instancia}'

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()


MiClase.metodo_clase()
miObjeto1 = MiClase('Variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()
