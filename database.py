from select import select
from traceback import print_tb
import pymysql
from pyparsing import ExceptionWordUnicode

try:
    conexion = pymysql.connect( host='localhost',
                                user='root',
                                password='',
                                db='peliculas')

    print("Conexión correcta")

    try:
        # insert
        # with conexion.cursor() as cursor:
        #     consulta = "INSERT INTO peliculas (titulo, anio) values (%s, %s);"
        #     titulo = input("titulo: ")
        #     anio = int(input("anio: "))
        #     cursor.execute(consulta, (titulo, anio))
        # conexion.commit()
        
        # select
        select = input("select? ")
        if (select == ""):

            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM peliculas;")

                # con fetchall se traen en tupla de tuplas
                peliculas = cursor.fetchall()

                # para imprimir
                for pelicula in peliculas:
                    print(pelicula)

                cursor.execute("SELECT last_insert_id();")
                id = cursor.fetchone()
                print("###########################")
                print((pelicula)[0])


    finally:
        conexion.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)

