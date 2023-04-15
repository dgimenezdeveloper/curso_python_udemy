from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPelicula as cp


opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1.- Agregar Película ')
        print('2.- Listar Película ')
        print('3.- Eliminar catálogo películas ')
        print('4.- Salir ')
        opcion = int(input('Escribe tu opción: (1 - 4): '))

        if opcion == 1:
            nombre_pelicula = input('Ingresa el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        print(f'Ingrese una opción valida...'.upper())
        opcion = None
else:
    print('Salimos del programa...')
