import os 
from dominio.Pelicula import Pelicula


class CatalogoPelicula():
    ruta_archivo = 'peliculas.txt'
    
    @classmethod
    def agregar_pelicula(cls, pelicula: Pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'Nombre de la Película: \t* {pelicula.nombre}\n')
    
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f' Catálogo de Películas '.center(50, '*'))
            print(archivo.read())
        
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Se ha eliminado el archivo: {cls.ruta_archivo}')