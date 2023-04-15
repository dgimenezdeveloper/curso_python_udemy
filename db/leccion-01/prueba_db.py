import psycopg2

conexion = psycopg2.connect(
    user="daseg", password="15211730", host="localhost", port="5432", database="test_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # FETCHALL
            """sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
            # llaves_primarias = ((1, 2, 3),)
            # id_persona = input('Proporciona el valor id_persona: ')
            entrada = input('Proporciana los id\'s a buscar (separados por comas) : ' )
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)"""
            # Insertar Registro

            """ sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(sentencia, valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}') """

            # iNSERTAR VARIOS REGISTROS
            """ sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)"
            valores = (
                ("Marcos", "Cantu", "mcantu@mail.com"),
                ("Angel", "Quintana", "aquintana@mail.com"),
                ("Maria", "Gonzalez", "mgonzalez@mail.com")
            )
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f"Registros Insertados: {registros_insertados}") """

            # ACTUALIZAR UN REGISTRO
            """ sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = ("Juan Carlos", "Juarez", "jcjuarez@mail.com", 1)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros Actualizados: {registros_actualizados}") """

            # ACTUALIZAR VARIOS REGISTROS
            """ sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = (
                ("Juan", "Perez", "jperez@mail.com", 1),
                ("Ivonne", "Gutierrez", "igutierrez@mail.com", 2),)
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros Actualizados: {registros_actualizados}") """
            
            # ELIMINAR UN REGISTRO
            """ sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Proporciona el id_persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros Eliminados: {registros_actualizados}") """
            
            # ELIMINAR VARIOS REGISTROs
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar(separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros Eliminados: {registros_actualizados}")

except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()
