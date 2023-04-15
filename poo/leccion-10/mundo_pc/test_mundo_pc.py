from raton import Raton
from monitor import Monitor
from teclado import Teclado
from computadora import Computadora
from orden import Orden


teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Hp', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('ACER', 'Bluetooth')
raton2 = Raton('ACER', 'Bluetooth')
monitor2 = Monitor('ACER', 27)
computadora2 = Computadora('ACER', monitor2, teclado2, raton2)

teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', 34)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadoras(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)