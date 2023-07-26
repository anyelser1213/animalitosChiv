
#Esto lo creamos nosotros para mayor organizacion
import sqlite3

from animalitoschinos.settings import BASE_DIR

# Conexion al servidor de PostgreSQL
def todoSqlite3():

    prueba= BASE_DIR / 'db.sqlite3'
    print()
    conexion=sqlite3.connect(prueba)
    print(conexion)
    try:
        print("Entramos aqui...")
        conexion.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='resultados_resultados';")
        print("se creo la tabla articulos")                        
    except sqlite3.OperationalError:
        print("No Hubo Conexion")                    
    conexion.close()
    