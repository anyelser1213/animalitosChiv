import datetime
import calendar

#Es necesario importar las dependendias necesarias
from datetime import date

#otras librerias
from datetime import datetime
from datetime import timedelta

#Funcion para tener las fechas de la semana
def fecha_I_F():

    now = datetime.now()
    print("fecha de hoy: ",now)
    retroceso = now.weekday()
    fecha_inicio = now+timedelta(days=-retroceso)
    print("fecha inicio de semana:",fecha_inicio)
    print("fecha final de semana:",fecha_inicio+timedelta(days=6))

    return str(fecha_inicio.strftime("%d/%m/%Y")),str((fecha_inicio+timedelta(days=6)).strftime("%d/%m/%Y"))


#Con esta funcion mostramos las fechas de la semana pasada
def fecha_I_F_anterior(fecha):

    now = datetime.strptime(fecha, '%d/%m/%Y')
    print("fecha de hoy: ",now)
    fecha_inicio = now+timedelta(days=-7)
    print("fecha inicio de semana:",fecha_inicio)
    print("fecha final de semana:",fecha_inicio+timedelta(days=6))

    return str(fecha_inicio.strftime("%d/%m/%Y")),str((fecha_inicio+timedelta(days=6)).strftime("%d/%m/%Y"))

#Con esta funcion mostramos las fechas de la semana siguiente
def fecha_I_F_siguiente(fecha):

    now = datetime.strptime(fecha, '%d/%m/%Y')
    print("fecha de hoy: ",now)
    fecha_inicio = now+timedelta(days=+7)
    print("fecha inicio de semana:",fecha_inicio)
    print("fecha final de semana:",fecha_inicio+timedelta(days=6))

    return str(fecha_inicio.strftime("%d/%m/%Y")),str((fecha_inicio+timedelta(days=6)).strftime("%d/%m/%Y"))


#Adaptar para los datatime
def conversionValida(fecha):

    fecha_conversion = fecha.replace('_','/') 
    return fecha_conversion

def calendarioPruebas():

    

    now = datetime.now()
    print("fecha de hoy: ",now)
    retroceso = now.weekday()
    fecha_inicio = now+timedelta(days=-retroceso)
    print("fecha inicio de semana:",fecha_inicio)
    print("fecha final de semana:",fecha_inicio+timedelta(days=6))
    

    #print (calendar.calendar(2023,7,28,6))

def informacionCalendario():


    #Sumar dos días a la fecha actual
    now = datetime.now()
    print("--------------")
    print(now)
    print("dia semana: ",now.weekday())
    new_date = now + timedelta(days=2)
    print(new_date)
    print("---------------")

    #######################################


    #Tiempo actual
    tiempo = datetime.now()
    print("Año:",tiempo.year)
    print("Mes:",tiempo.month)
    print("dia:",tiempo.day)

    print(list(calendar.day_name))
    print("------")
    #print(list(calendar.month_name))

    print("------")

    print("Calendario de Marzo 2023")
    #print(calendar.month(tiempo.year,tiempo.month))


    print("Calendario de la semana 2023")

    numero_semana = tiempo.isocalendar()
    print("Todo: ",numero_semana)
    print("Numero de la semana actual: ",numero_semana[1])
    #lunes = 0
    print("Numero del dia de la semana: ",(calendar.weekday(tiempo.year,tiempo.month,tiempo.day)))

    #dia de la semana
    print(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])

    #print(calendar.firstweekday())


#Funciones para las fechas
def dia_mes_actual(): 

    #Día actual
    fecha = date.today()
    #Date
    #print("El día actual es {}".format(fecha.day))
    #print("El mes actual es {}".format(fecha.month))
    #print("El año actual es {}".format(fecha.year))
    #print("PROBAMOS AQUI", fecha)

    ultimo_dia = calendar.monthrange(fecha.year,fecha.month)[1]
    #print(f'{ultimo_dia}/{fecha.month}/{fecha.year}')
    #next_month = any_day.replace(day=28) + datetime.timedelta(days=4) # this will never fail return next_month - datetime.timedelta(days=next_month.day)
    return f'{fecha.day}/{fecha.month}/{fecha.year}'


#Con esta funcion traemos el mes actual para solo traer las del dia de hoy
def dia_mes_actual_consultas(): 

    #Día actual
    fecha = date.today()
    #Date
    #print("El día actual es {}".format(fecha.day))
    #print("El mes actual es {}".format(fecha.month))
    #print("El año actual es {}".format(fecha.year))
    #print("PROBAMOS AQUI", fecha)

    ultimo_dia = calendar.monthrange(fecha.year,fecha.month)[1]
    #print(f'{ultimo_dia}/{fecha.month}/{fecha.year}')
    #next_month = any_day.replace(day=28) + datetime.timedelta(days=4) # this will never fail return next_month - datetime.timedelta(days=next_month.day)
    return f'{fecha.year}-{fecha.month}-{fecha.day}'