from Vehiculo import *

vehiculo1 = Vehiculo('Negro', 5)
print('Creación Vehiculo'.center(50, '*'))
print(vehiculo1)


coche1 = Coche('Rojo', 4, 240)
print('Creación Coche'.center(50, '*'))
print(coche1)

bicicleta1 = Bicicleta('Azul', 2, 'montainBike')
print('Creación Bicicleta'.center(50, '*'))
print(bicicleta1)

# Modificar atributos
vehiculo1.color = 'Morado'
vehiculo1.ruedas = 1
print(vehiculo1)