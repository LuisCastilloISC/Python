from Persona import Persona
from Conexion import Conexion
from cursorDelPool import CursorDelPool
from logger_base import log
class PersonaDao:

    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre,apellido,email,edad) Values(%s,%s,%s,%s)"
    _ACTUALIZAR ="UPDATE persona SET nombre=%s,apellido=%s, email=%s,edad=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas =[]
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3],r[4])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre,persona.Apellido, persona.Email,persona.Edad)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre,persona.Apellido, persona.Email,persona.Edad,persona.idPersona)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount


if __name__ == "__main__":
    #Insertar
    persona1 = Persona(nombre="Pancrasio",apellido="Mendez",email="pmendez@mail.com",edad=23)
    personasInsertadas = PersonaDao.insertar(persona1)
    log.debug(f"Personas insertadas {personasInsertadas}")
    #Actualizar
    persona1 = Persona(id_persona=2,nombre="Pancrasio",apellido="Mendez",email="pmendez@mail.com",edad=23)
    personasActualizadas = PersonaDao.actualizar(persona1)
    log.debug(f"Personas actualizadas {personasActualizadas}")
    #eliminar
    persona1 = Persona(id_persona=10)
    personasEliminadas = PersonaDao.eliminar(persona1)
    log.debug(f"Personas eliminadas {personasEliminadas}")
    #ver
    personas = PersonaDao.seleccionar()
    for p in personas:
        log.debug(p)



