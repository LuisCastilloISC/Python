from random import seed
from logger_base import log
from Conexion import Conexion

class CursorDelPool:
        def __init__(self) -> None:
            self._conexion=None
            self._cursor =None
        
        def __enter__(self):
            log.debug("Inicio metodo with")
            self._conexion = Conexion.ObtenerConexion()
            self._cursor=self._conexion.cursor()
            return self._cursor
        
        def __exit__(self,tipo_excepcion,valor_excepcion,detalle_excepcion):
            log.debug("Se ejecuta exit")
            if valor_excepcion:
                self._conexion.rollback()
            else:
                self._conexion.commit()
            self._cursor.close()
            Conexion.LiberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())