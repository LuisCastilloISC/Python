
from logger_base import log

class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None,edad=None) -> None:
        self.id_persona = id_persona
        self._nombre=nombre
        self._apellido=apellido
        self._email=email
        self._edad = edad
    
    def __str__(self) -> str:
        return f'''
            ID Persona: {self.id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}
        '''
    @property
    def idPersona(self):
        return self.id_persona
    
    @idPersona.setter
    def idPersona(self,id_persona):
        self.id_persona=id_persona

    @property
    def Nombre(self):
        return self._nombre
    
    @Nombre.setter
    def Nombre(self,nombre):
        self._nombre=nombre
    
    @property
    def Apellido(self):
        return self._apellido
    
    @Apellido.setter
    def Apellido(self,apellido):
        self._apellido=apellido

    @property
    def Email(self):
        return self._email
    
    @Email.setter
    def Email(self,email):
        self._email=email

    @property
    def Edad(self):
        return self._edad
    
    @Edad.setter
    def Edad(self,edad):
        self._edad= edad

if __name__ == '__main__':
    persona1 = Persona(1,'JUAN','PEREZ','jperex@mail.com')
    log.debug(persona1)
    #settear Valor NONE default
    persona1  = Persona(nombre='Juan',apellido='Perez',email='jperez@emai.com')
    log.debug(persona1)
    #simular delete
    persona1 = Persona(id_persona=1)