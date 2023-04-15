from logger_base import log
class Usuario:
    def __init__(self, id: int=None, username: str=None, password: str=None) -> None:
        self._id = id
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return f'''
        ID N°: {self._id}
        USUARIO: {self._username}
        PASSWORD: {self._password}
    '''
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id
    
    @property
    def usuario(self):
        return self._username
    
    @usuario.setter
    def usuario(self, usuario: str):
        self._username = usuario
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password: str):
        self._password

if __name__ == '__main__':
    usuario1 = Usuario(2,'miguel', '15091998')
    log.debug(usuario1)
