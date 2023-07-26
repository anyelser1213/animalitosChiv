#Esto lo creamos nosotros para mayor organizacion
import psycopg2


#llamamos a la funcion conexion
from aplicaciones.principal.BD_POSTGRES_DINAMICA.conexion import conexion



#Funcion para ingresar datos a la tabla de hoy
def insertarDatosTabla(nombreTabla,tipo_jugada,id_jugada,id_telefono,id_usuario,id_comprobante,status,fecha_creacion):
    """ Conexión al servidor de pases de datos PostgreSQL """

    conexionActiva = conexion()
    #Aqui verificamos la conexion
    if conexionActiva is not None:
        print("Estamos conectados, DATOS A INSERTAR:")
        print("digito: ",id_jugada)
        print("telefono: ",id_telefono)
        print("comprobante: ",id_comprobante)
        print("usuario: ",id_usuario)
        print("status: ",status)
        print("fecha_creacion: ",fecha_creacion)

        #Cursor
        cursor = conexionActiva.cursor()
        #print(conexionActiva)
        #print(cursor)

        #Cosas que modificaremos
        #nombreTabla = str(nombreTabla).replace("-","_")
        #nombreTabla = "tabla_"+str(nombreTabla)

        #Valores a usar
        print("Entramos a ver si existe la tabla:",nombreTabla)
        #verificarTabla = "SELECT table_name FROM information_schema.tables WHERE table_schema='pubdlic';"
        verificarTabla = "{}".format("select tablename from pg_tables where schemaname='public';")
        print("Consulta:",verificarTabla)                              
        #verificarTabla = "{}'{}'{}".format('select * from pg_tables where tablename=',nombreTabla,";")
        #cursor.execute(verificarTabla)

        
        #Ejecutamos la consulta
        cursor.execute(verificarTabla)
        #print("Tabla: ",)
        #iteramos sobre los resultados
        ya_existe =False #Esta variable es para comprobar si existe o no
        for fila in cursor:
            if fila.count(nombreTabla):
                print("Encontrado...")
                ya_existe = True
                break
            else:
                pass
            #print(fila)
        #resultadoTupla = cursor.fetchall()
        #print("Resultado tupla:",resultadoTupla)
        #print("Resultado existe:",resultadoTupla.count(nombreTabla))
        #print("Tabla fetchone: ",type(resultadoTupla))
        #print("resultado: ",resultadoVerificar)

        
        

        #Si no existe la creamos aqui....
        if ya_existe: # Make an API request.
            
            print("Esta tabla ya existe: "+nombreTabla)

            #insertar datos a la tabla(configuracion estandar de la tabla)
            consulta = "insert into {} (tipo_jugada,digito,telefono,comprobante,usuario,status,fecha_creacion) values('{}',{},'{}',{},'{}','{}','{}');".format(str(nombreTabla),str(tipo_jugada),id_jugada,id_telefono,id_comprobante,id_usuario,status,fecha_creacion)
            
            #Ejecutamos la consulta
            cursor.execute(consulta)
            print("Datos insertados...")
            
        else:


            #AQUI CREAMOS LA TABLA CORRESPONDIENTE
            print("-------------------------")
            print(verificarTabla)
            #print("Probamos aqui para crear.....",cursor.execute(str(verificarTabla)))
            print("-------------------------")

            
        #print(cursor.execute(verificarTabla))
        
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
    



