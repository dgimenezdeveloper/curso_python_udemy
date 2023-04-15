from logger_base import log
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE = "usuarios"
    _USERNAME = "daseg"
    _PASSWORD = "15211730"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE,
                )
                log.debug(f"\nConexión exitosa del pool:\n{cls._pool}\n")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrió un error al obtener el pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"\nConexión obtenida del pool:\n{conexion}\n")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"\nSe regresa la conexión al pool:\n{conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == "__main__":
    conexion_uno = Conexion.obtenerConexion()
    conexion_dos = Conexion.obtenerConexion()
    conexion_tres = Conexion.obtenerConexion()
    conexion_cuatro = Conexion.obtenerConexion()
    conexion_cinco = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_cinco)
    conexion_seis = Conexion.obtenerConexion()
