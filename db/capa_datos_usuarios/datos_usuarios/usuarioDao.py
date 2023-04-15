from usuario import Usuario
from logger_base import log
from CursorDelPool import CursorDelPool


class UsuarioDao:
    _SELECCIONAR = "SELECT * FROM tabla_usuarios ORDER BY id"
    _INSERTAR = "INSERT INTO tabla_usuarios (username, password) VALUES(%s,%s)"
    _ACTUALIZAR = "UPDATE tabla_usuarios SET username=%s, password=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM tabla_usuarios WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros_tabla = cursor.fetchall()
            lista_usuarios = []
            for registro in registros_tabla:
                usuario = Usuario(registro[0], registro[1], registro[2])
                lista_usuarios.append(usuario)
            return lista_usuarios
        
    @classmethod
    def insertar(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            datos = (usuario.usuario, usuario.password)
            cursor.execute(cls._INSERTAR, datos)
            log.debug(f'Usuario agregado: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            datos = (usuario.usuario, usuario.password, usuario.id)
            cursor.execute(cls._ACTUALIZAR, datos)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            datos = (usuario.id,)
            cursor.execute(cls._ELIMINAR, datos)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount
    
if __name__ == '__main__':
    # usuario_2 = Usuario(username='daseg210986',password='gmnz152117')
    # usuario_3 = Usuario(username='miguelcid',password='cidmiguel')
    
    # usuarios_insertados = UsuarioDao.insertar(usuario_3)
    # log.debug(f'Usuario Agregado: {usuarios_insertados}')
    
    # usuarios = UsuarioDao.seleccionar()
    # for usuario in usuarios:
    #     log.debug(usuario)
    
    persona1 = Usuario(id=4)
    personas_eliminadas = UsuarioDao.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')