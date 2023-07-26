
#Esto lo creamos nosotros para mayor organizacion
import psycopg2

#Aqui llamados a las variables 
from aplicaciones.principal.BD_POSTGRES_DINAMICA import VARIABLES

#llamamos a la funcion conexion
from aplicaciones.principal.BD_POSTGRES_DINAMICA.conexion import conexion


#CCREATE CREAR
#READ...LEER
#UPDATE...ACTUALIZAR
#DELETE...BORRAR


#Funcion para insertarDatos
def insertarDatos():
    """ Conexión al servidor de pases de datos PostgreSQL """
     # creación del cursor

    