from usuarioDao import UsuarioDao
from usuario import Usuario
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1 - Listar Usuarios: ')
    print('2 - Agregar Usuario: ')
    print('3 - Modificar Usuario: ')
    print('4 - Eliminar Usuario: ')
    print('5 - Salir: ')
    opcion = int(input('Elige una opciṕn: '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Ingrese el username: ')
        password_var = input('Ingrese el username: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios Insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_var = int(input('Escribe el id  a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo passqord: ')
        usuario = Usuario(id_var, username_var,password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_var = int(input('Escribe el id a eliminar: '))
        usuario = Usuario(id = id_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
    else: log.info('Salimos de la aplicación... :D')