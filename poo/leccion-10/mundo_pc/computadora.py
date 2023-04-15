from raton import Raton
from monitor import Monitor
from teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre: str, monitor: Monitor, teclado: Teclado, raton: Raton) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self) -> str:
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Hp', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado('ACER', 'Bluetooth')
    raton2 = Raton('ACER', 'Bluetooth')
    monitor2 = Monitor('ACER', 27)
    computadora2 = Computadora('ACER', monitor2, teclado2, raton2)
    print(computadora2)