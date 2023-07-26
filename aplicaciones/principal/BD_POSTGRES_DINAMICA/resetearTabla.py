#Esto lo creamos nosotros para mayor organizacion
import psycopg2


#llamamos a la funcion conexion
from aplicaciones.principal.BD_POSTGRES_DINAMICA.conexion import conexion



#Funcion para resetear una tabla puntual
def resetearTabla(nombreTabla):
    """ Conexión al servidor de pases de datos PostgreSQL """

    conexionActiva = conexion()
    #Aqui verificamos la conexion
    if conexionActiva is not None:
        print("Estamos conectados, RESETEANDO:")

        #Cursor
        cursor = conexionActiva.cursor()
        #print(conexionActiva)
        #print(cursor)
        
        #insertar datos a la tabla(configuracion estandar de la tabla)
        consulta = "ALTER SEQUENCE "
            
        #Ejecutamos la consulta
        cursor.execute(consulta)
        print("Datos insertados...")
            
        
        conexionActiva.close()

        

        


    #Este else es en caso de que no pudimos conectarnos a la base de datos
    else:
        print("No estamos conectados")
    #print("Conexion: ",VARIABLES.conexion)
    
    """
    cursor = conexion.cursor()
        
    # Ejecución de una consulta con la version de PostgreSQL
    print('La version de PostgreSQL es la:')
    cursor.execute('SELECT version();')


    query = "CREATE TABLE power(nombre varchar(30));"
    cursor.execute(query)    
    # Cierre de la comunicación con PostgreSQL
    conexion.close()

    """
    



