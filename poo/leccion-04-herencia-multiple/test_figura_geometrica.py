from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

#NO se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creación Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='Rojo')
cuadrado1.ancho = 9
print(cuadrado1)

print('Creación Objeto Rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='azul')
rectangulo1.ancho = 15
print(rectangulo1)
