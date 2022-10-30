

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
            sentencia = "INSERT INTO cliente(nombre,apellido,email) Values(%s,%s,%s)"
            # valores = ("Humberto","rivera","hrivera@mail.com")
            # cursor.execute(sentencia,valores)
            valores = (
                ("Marcos","Cantu","mcantu@mail.com"),
                ("Angel","lopez","alopez@mail.com"),
                ("Pedro","Garcia","pgarcia@mail.com")
                )
            cursor.executemany(sentencia,valores)
            registrosInsertados = cursor.rowcount
            log.debug(f"Registros insertados: {registrosInsertados}") 
except Exception as e:
    log.error(e)
finally:
    conexion.close()
            #sentencia="SELECT * FROM cliente WHERE id_usuario=%s"
            # idUsuario = input("Proporcione el ID del cliente")
            # cursor.execute(sentencia,(idUsuario,))
            # resultado = cursor.fetchone()
            # print(resultado)