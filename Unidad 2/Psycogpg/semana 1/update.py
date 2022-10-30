

import psycopg2
from logger_base import log
conexion =psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port ="5432",
    database="clase_db")
print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE cliente SET nombre = %s ,apellido = %s ,email =%s WHERE id_usuario = %s"
            valores =(
                ("Pancracio","Hernandez","phernandez@mail.com",2),
                ("Lupita","Garcia","lgarcia@mail.com",1)
            )
            cursor.executemany(sentencia,valores)
            registrosActualizados = cursor.rowcount
            log.debug(f'Registros Actualizados: {registrosActualizados}')

except Exception as e:
    log.error(e)
finally:
    conexion.close()
           