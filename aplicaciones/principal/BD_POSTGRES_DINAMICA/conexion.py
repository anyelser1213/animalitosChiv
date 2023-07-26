
#Esto lo creamos nosotros para mayor organizacion
import psycopg2
from aplicaciones.principal.BD_POSTGRES_DINAMICA import VARIABLES

# Conexion al servidor de PostgreSQL
def conexion():

    try:
        #nombreBD = "relancino"
        #usuario = "postgres"
        #clave = "postgres"
        #HOSTting = "localhost"
        #PORT = "5432"

        #Esto es la conexion
        conexion = psycopg2.connect(host=VARIABLES.HOSTING, database=VARIABLES.NOMBREBD, user=VARIABLES.USUARIO, password=VARIABLES.CLAVE,port=VARIABLES.PUERTO)
        
        #No se que hace esto
        conexion.autocommit = True


        print("Conexion exitosa")

        return conexion


    except Exception as ex:

        print("Conexion Fallida", ex)
        return None
    