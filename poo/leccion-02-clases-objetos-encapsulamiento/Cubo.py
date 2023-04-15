class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho*self.alto*self.profundidad


def solicitar_datos():
    base = int(input('Proporciona el ancho: '))
    altura = int(input('Proporciona la altura: '))
    profundidad = int(input('Proporciona la profundidad: '))
    return altura, base, profundidad


if __name__ == '__main__':
    base,altura,profundidad = solicitar_datos()
    cubo1=Cubo(base,altura,profundidad)
    print(f'Volumen del cubo: {cubo1.calcular_volumen()}')