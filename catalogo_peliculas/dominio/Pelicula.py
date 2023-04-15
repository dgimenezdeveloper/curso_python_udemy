class Pelicula:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
    
    def __str__(self) -> str:
        return f'Nombre de la Película: {self._nombre}'
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

if __name__ == '__main__':
    pelicula1 = Pelicula('Saw')
    print(pelicula1.nombre)