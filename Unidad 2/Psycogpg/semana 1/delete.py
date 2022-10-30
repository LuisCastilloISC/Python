

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
            sentencia = "DELETE FROM cliente WHERE id_usuario IN (6,8,9,10)"
            entrada = input("IDs A ELIMINAR:")
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registrosEliminados = cursor.rowcount
            log.debug(f"Registros Eliminados:{registrosEliminados}")

except Exception as e:
    log.error(e)
finally:
    conexion.close()
           