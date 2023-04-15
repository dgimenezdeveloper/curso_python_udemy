from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho: int, alto: int, color: str):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self._ancho*self._alto
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} - {Color.__str__(self)} - Área: {Rectangulo.calcular_area(self)}'