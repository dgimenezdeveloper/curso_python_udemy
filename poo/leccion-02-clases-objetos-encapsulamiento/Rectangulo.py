class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    
    def calcular_area(self):
        return self.altura*self.base

def solicitar_datos():
    base = int(input('Proporciona la base: '))
    altura = int(input('Proporciona la altura: '))
    return altura, base

if __name__ == '__main__':
    altura, base = solicitar_datos()
    rectangulo1 = Rectangulo(altura, base)
    print(f'Área del Rectángulo: {rectangulo1.calcular_area()}')