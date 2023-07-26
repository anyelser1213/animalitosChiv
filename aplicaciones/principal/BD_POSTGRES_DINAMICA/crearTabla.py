#Esto lo creamos nosotros para mayor organizacion
import psycopg2

#Estas variables y funcion estan para todo el crud de tablas dinamicas
from aplicaciones.principal.BD_POSTGRES_DINAMICA import VARIABLES
#from aplicaciones.principal.BD_POSTGRES_DINAMICA.VARIABLES import NombreTablaDeHoy
from aplicaciones.principal.BD_POSTGRES_DINAMICA.conexion import conexion


#CCREATE CREAR
#READ...LEER
#UPDATE...ACTUALIZAR
#DELETE...BORRAR


#Funcion para crear la tabla
def crearTabla(nombreTabla):
    """ PRIMERO Conexión al servidor de bases de datos PostgreSQL """
     

    conexionActiva = conexion()
    #Aqui verificamos la conexion
    if conexionActiva is not None:
        print("Estamos conectados")

        #Para que todas las transacciones se hagan automaticamente
        #VARIABLES.conexion.autocommit = True
        #VARIABLES.conexion.close()

        # creación del cursor
        cursor = conexionActiva.cursor()
        #print(VARIABLES.conexionActiva)
       
        #print(cursor)

        #Cosas que modificaremos
        nombreTabla = str(nombreTabla).replace("-","_")
        nombreTabla = "tabla_"+str(nombreTabla)

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
            
            print("resultado: ")
            print("Esta tabla ya existe: "+nombreTabla)

           
            
        else:


            #AQUI CREAMOS LA TABLA CORRESPONDIENTE
            print("-------------------------")
            print(verificarTabla)
            #print("Probamos aqui para crear.....",cursor.execute(str(verificarTabla)))
            print("-------------------------")

            #Creacion de la tabla(configuracion estandar de la tabla)

            """
            consulta = "create table {}("\
                "id BIGSERIAL PRIMARY KEY,"\
                "id_jugadas int,"\
                "id_telefono int,"\
                "id_comprobante int,"\
                "id_usuario int,"\
                "status character varying(150),"\
                "fecha_creacion timestamp with time zone,"\
                "constraint fk_id_jugadas foreign key (id_jugadas) references juegos_jugada (id) ON DELETE CASCADE,"\
                "constraint fk_id_telefono foreign key (id_telefono) references juegos_telefono (id) ON DELETE CASCADE,"\
                "constraint fk_id_comprobante foreign key (id_comprobante) references juegos_comprobante (id) ON DELETE CASCADE,"\
                "constraint fk_id_usuario foreign key (id_usuario) references usuarios (id) ON DELETE CASCADE"\
                ");".format(str(nombreTabla))
            """

            consulta = "create table {}("\
                "id BIGSERIAL PRIMARY KEY,"\
                "tipo_jugada character varying(150),"\
                "digito int,"\
                "telefono character varying(150),"\
                "comprobante int,"\
                "usuario character varying(150),"\
                "status character varying(150),"\
                "fecha_creacion timestamp with time zone);".format(str(nombreTabla))

            #Ejecutamos la consulta
            cursor.execute(consulta)


            #Truncamos la tabla de jugadas_del_dia(con esto reseteamos desde cero esta tabla incluyendo el id)
            consulta = "truncate table juegos_jugadas_del_dia restart identity;"
            #Ejecutamos la consulta
            cursor.execute(consulta)


            print("Table {} CREADA.".format(nombreTabla))
        #print(cursor.execute(verificarTabla))
        
        conexionActiva.close()

        #Esto lo enviamos para almacenar el nombre en su modelo
        return nombreTabla

        


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
    



