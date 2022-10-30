#pip install psycopg2

import psycopg2

conexion = psycopg2.connect(user="postgres"
                            ,password="admin"
                            ,host="127.0.0.1"
                            ,port="5432"
                            ,database="clase_db")
print(conexion)
cursor = conexion.cursor()
cursor.execute("SELECT nombre FROM cliente")
resultados = cursor.fetchone()
print(resultados)
