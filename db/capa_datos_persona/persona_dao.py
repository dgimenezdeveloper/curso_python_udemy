from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona: Persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount # Retorna Cantidad de Registros Insertados
    
    @classmethod
    def actualizar(cls, persona: Persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido,persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, persona: Persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount
    
if __name__ == '__main__':
    # INSERTAR UN REGISTRO
    persona1 = Persona(nombre='Alejandra', apellido='Tellez', email='atellez@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'persona insertada: {personas_insertadas}')
    
    # # ACTUALIZAR UN REGISTRO
    # persona1 = Persona(1,'Juan','Perez', 'jperez@email.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas Actualizadas: {personas_actualizadas}')
    
    # # Eliminar un registro
    # persona1 = Persona(id_persona=13)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')
    
    # # SELECCIONAR OBJETOS
    # personas = PersonaDAO.seleccionar()
    # for persona in personas:
    #     log.debug(persona)