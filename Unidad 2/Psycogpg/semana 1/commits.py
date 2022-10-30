
import psycopg2
from logger_base import log
conexion = psycopg2.connect(user="postgres"
                            ,password="admin"
                            ,host="127.0.0.1"
                            ,port="5432"
                            ,database="clase_db")
print(conexion)

try:
    conexion.autocommit=False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO cliente(nombre,apellido,email) Values(%s,%s,%s)"
    nombre ='Juan'
    valores = (nombre,'Perez','jperez@gmail.com')
    
    cursor.execute(sentencia,valores)
    log.debug("Sentencia Insert")
    sentencia = "UPDATE cliente SET nombre=%s , apellido=%s, email=%s WHERE id_usuario=%s"
    valores=("Hugo","sanchez","hsanchez@mail.com",1)
    cursor.execute(sentencia,valores)
    log.debug("Sentencia Update")
    conexion.commit()
    log.debug("Cambios guardados")
except Exception as e:
    conexion.rollback()
    log.error(e)


try:
    conexion.autocommit=False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO cliente(nombre,apellido,email) Values(%s,%s,%s)"
    nombre ='Juan'
    valores = (nombre,'Perez','jperez@gmail.com')
    
    cursor.execute(sentencia,valores)
    log.debug("Sentencia Insert")
    sentencia = "UPDATE cliente SET nombre=%s , apellido=%s, email=%s WHERE id_usuario=%s"
    valores=("Hugo","sanchez","hsanchez@mail.com",1)
    cursor.execute(sentencia,valores)
    log.debug("Sentencia Update")
    conexion.commit()
    log.debug("Cambios guardados")
except Exception as e:
    conexion.rollback()
    log.error(e)



