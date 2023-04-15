try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # print(archivo.read())
    # print(archivo.read(9)) #Leer algunos caracteres
    # print(archivo.readline())#Leer lineas completas

    # Iterar el archivo
    # for linea in archivo:
    #     print(linea)

    # Leer lineas
    # print(archivo.readlines())
    
    # Acceder a una linea de la lista
    # print(archivo.readlines()[0])
    
    # Abrimos un nuevo archivo
    # a - anexar informacion
    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())

except Exception as e:
    print(e)
finally:
    print('Se ha terminado el proceso de leer y copiar archivos')
    archivo.close()
    archivo2.close()
    print('Los archivos han sido cerrados correctamente.')
