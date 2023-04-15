from computadora import Computadora

class Orden:
    contador_ordenes = 0
    
    def __init__(self, computadoras: Computadora) -> None:
        Orden.contador_ordenes +=1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras
    
    def agregar_computadoras(self, computadora):
        self._computadoras.append(computadora)
    
    def __str__(self) -> str:
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'''
            Orden: {self._id_orden}
            Computadora: {computadoras_str}
    '''