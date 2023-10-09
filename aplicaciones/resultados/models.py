from django.db import models

#Funciones creadas
from aplicaciones.resultados.funciones import dia_mes_actual

from animalitoschinos.settings import MEDIA_URL, STATIC_URL

#Para establecer fechas y horarios por defectos
from datetime import datetime
from datetime import time
import calendar
import locale

from django.utils import timezone
#from django.utils.timezone import now


def calcularIncremento():
    #print(Resultados.objects.all())
    cantidad = 1 # int(Resultados.objects.all().count()+1)
    return int(Resultados.objects.all().count()+1)

#establecer Dia actual
def establecerDiaActual():

    #Este locale es para cambiar el idioma al español
    locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")
    tiempo = datetime.now()
    
    #dia de la semana
    print("dia de hoy:",calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])
    cantidad = 1 # int(Resultados.objects.all().count()+1)
    print(Dia.objects.filter(dia_semana=str(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])))
    return Dia.objects.get(dia_semana=str(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])).id


#establecer Hora Siguiente de los resultados
def establecerHoraActual():

    #Este locale es para cambiar el idioma al español
    locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")
    tiempo = datetime.now()
    #print("Numero de la semana actual: ",numero_semana[1])

    #print("-----------------------------")
            


    #Ingresando num de semana
    #self.semana = datetime(self.fecha_resultado.year, self.fecha_resultado.month, self.fecha_resultado.day, 00, 00, 00, 0).isocalendar()[1]

    #lunes = 0
    #print("Numero del dia de la semana: ",(calendar.weekday(tiempo.year,tiempo.month,tiempo.day)))

    #dia de la semana
    #print(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])
    
    #numero semana
    semana_actual = datetime(tiempo.year, tiempo.month, tiempo.day, 00, 00, 00, 0).isocalendar()[1]

    #dia actual
    dia_hoy = Dia.objects.get(dia_semana=str(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])).id

    """
    hora_11_00 = Hora.objects.get(hora=time(11,0,00))
    hora_12_00 = Hora.objects.get(hora=time(12,0,00))
    hora_01_00 = Hora.objects.get(hora=time(13,0,00))
    hora_04_00 = Hora.objects.get(hora=time(16,0,00))
    hora_07_00 = Hora.objects.get(hora=time(19,0,00))
    """

    hora_12_00 = Hora.objects.get(hora=time(12,0,00))
    hora_01_00 = Hora.objects.get(hora=time(13,0,00))
    hora_04_00 = Hora.objects.get(hora=time(16,0,00))
    hora_07_00 = Hora.objects.get(hora=time(19,0,00))
    hora_11_00 = Hora.objects.get(hora=time(23,0,00))

    print("semana:", semana_actual)


    print("12:00pm: ",Resultados.objects.filter(semana=int(semana_actual),dia=dia_hoy,hora=hora_12_00.id).count())
    
    #Comenzamos los condicionales
    #hoy con la hora de las 12:00pm
    if Resultados.objects.filter(semana=int(semana_actual),dia=dia_hoy,hora=hora_12_00.id).count() < 1:
        print("Probando con las 12:00pm")
        return hora_12_00.id
    
    #hoy con la hora de las 01:00pm
    elif Resultados.objects.filter(semana=int(semana_actual),dia=dia_hoy,hora=hora_01_00.id).count() < 1:
        print("Probando con las 01:00pm")
        return hora_01_00.id

    #hoy con la hora de las 04:00pm
    elif Resultados.objects.filter(semana=int(semana_actual),dia=dia_hoy,hora=hora_04_00.id).count() < 1:
        return hora_04_00.id

    #hoy con la hora de las 07:00pm
    elif Resultados.objects.filter(semana=int(semana_actual),dia=dia_hoy,hora=hora_07_00.id).count() < 1:
        return hora_07_00.id

    #hoy con la hora de las 11:00pm
    elif Resultados.objects.filter(semana=int(semana_actual),dia=dia_hoy,hora=hora_11_00.id).count() < 1:
        return hora_11_00.id

    else:
        print("Probando con las 12:00pm")
        return hora_12_00.id

    
    





    print(Dia.objects.filter(dia_semana=str(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])))
    return Dia.objects.get(dia_semana="miércoles").id



#Funcion para agregar carpetas al usuario
def imagen_animalitos(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    print(instance)
    print(instance.id)
    print(instance.nombre)
    return 'animalitos/{0}/{1}'.format(instance.nombre, filename)

def imagen_signos(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    print(instance)
    print(instance.id)
    print(instance.nombre)
    return 'signos/{0}/{1}'.format(instance.nombre, filename)

def imagen_numeros(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    print(instance)
    print(instance.id)
    print(instance.nombre)
    print("imagen_numero....")
    return 'numeros/{0}/{1}'.format(instance.nombre, filename)



############ MODELOS A USAR #######################

class Dia(models.Model):

    dia_semana_lista = [
        ('lunes','Lunes'),
        ('martes','Martes'),
        ('miércoles','Miercoles'),
        ('jueves','Jueves'),
        ('viernes','Viernes'),
        ('sábado','Sabado'),
        ('domingo','domingo'),
    ]
    dia_semana = models.CharField("Dia",max_length=30,choices=dia_semana_lista,default='normal',blank=False, null=False,unique=True)
    digito_dia_semana = models.PositiveSmallIntegerField(default=0)
    #imagen = models.ImageField("Imagen de Animalitos", upload_to=imagen_animalitos,default="media/perfil/default.png", max_length=200,blank=True,null=True)

    def __str__(self):
         return str(self.dia_semana)
    
    class Meta:

        verbose_name = "1.Dia"
        verbose_name_plural = "1.Dias"

    
    #Editando los metodos
    def save(self, *args, **kwargs): 

        #Colocamos el codigo de la semana internamente
        tiempo = datetime.now()
        dia_semana = calendar.weekday(tiempo.year,tiempo.month,tiempo.day)
        #print(dia_semana)

        #Este locale es para cambiar el idioma al español
        locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")
        diaPrueba = list(calendar.day_name)
        print("dia de hoy: ",diaPrueba)
        #print("Dia elegido: ",self.dia_semana)
        #self.digito_dia_semana = 0
        self.digito_dia_semana = diaPrueba.index(str(self.dia_semana))
            
        super(Dia, self).save(*args, **kwargs)
    


class Hora(models.Model):
    #nombre = models.CharField(max_length=30,unique=True)
    hora = models.TimeField(default=datetime.now(), blank=False,null=False)#Solo hora
    #imagen = models.ImageField("Imagen de Animalitos", upload_to=imagen_animalitos,default="media/perfil/default.png", max_length=200,blank=True,null=True)

    def __str__(self):
         return str(self.hora.strftime('%I:%M %p'))
    
    class Meta:

        verbose_name = "2.Hora"
        verbose_name_plural = "2.Horas"

    
    #Editando los metodos
    def save(self, *args, **kwargs): 

            
            super(Hora, self).save(*args, **kwargs)

class Animalitos(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    imagen = models.ImageField("Imagen de Animalitos", upload_to=imagen_animalitos,default="media/perfil/default.png", max_length=200,blank=True,null=True)

    def __str__(self):
         return self.nombre
    

    class Meta:

        verbose_name = "3.Animal"
        verbose_name_plural = "3.Animales"

class Signos(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    imagen = models.ImageField("Imagen de Signos", upload_to=imagen_signos,default="media/perfil/default.png", max_length=200,blank=True,null=True)


    def __str__(self):
         return self.nombre

    


    class Meta:

        verbose_name = "4.Signo"
        verbose_name_plural = "4.Signoss"


class Numeros(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    imagen = models.ImageField("Imagen de Numeros", upload_to=imagen_numeros,default="media/perfil/default.png", max_length=200,blank=True,null=True)


    def __str__(self):
         return self.nombre

    


    class Meta:

        verbose_name = "5.Numero"
        verbose_name_plural = "5.Numeros"


#aqui hacemos algo





class Resultados(models.Model):

    id = models.AutoField(primary_key=True)
    sorteo = models.PositiveIntegerField(default=calcularIncremento)

    #Para saber el dia y la hora
    #Aqui comenzamos los campos de resultados
    semana = models.PositiveIntegerField(blank=True,null=True)
    dia = models.ForeignKey(Dia,default=establecerDiaActual,on_delete=models.CASCADE, blank=False,null=False)
    hora = models.ForeignKey(Hora,default=establecerHoraActual,on_delete=models.CASCADE, blank=False,null=False)#Solo hora
    
    animalito = models.ForeignKey(Animalitos,on_delete=models.CASCADE,blank=False, null=False)
    #terminal= models.PositiveIntegerField(default=0)
    numero_foto = models.ForeignKey(Numeros,on_delete=models.CASCADE,blank=False, null=False)
    signo = models.ForeignKey(Signos,on_delete=models.CASCADE,blank=False, null=False)
    
    fecha_resultado = models.DateField(auto_now_add=False,auto_now=False,blank=False,default=dia_mes_actual) #Solo fecha


    def __str__(self):
         return str(self.sorteo)+" --- "+str(self.hora.__str__)+" --- "+str(self.animalito.nombre)+" --- "+str(self.numero_foto.nombre)+" --- "+str(self.signo.nombre)
    
    def obtenerImagenAnimalito(self):
      
        if self.animalito:
            return '{}{}'.format(MEDIA_URL,self.animalito)
        
    

    class Meta:

        verbose_name = "6.Resultado"
        verbose_name_plural = "6.Resultados"

        ordering = ('hora',)

    
    #Editando los metodos
    def save(self, *args, **kwargs): 

            #self.sorteo = self.sorteo + 1
            #self.auto_inc_id = Resultados.objects.all().count() + 1
            #Tiempo actual
            #Este locale es para cambiar el idioma al español
            #locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")
            #tiempo = datetime.now()
            #print("Numero de la semana actual: ",numero_semana[1])

            #print("-----------------------------")
            


            #print("----------------------------")
            #print("Pruebas:")
            #Argumentos son: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos.
            #print("fecha prueba1: ",datetime(2023, 7, 4, 10, 15, 00, 0).isocalendar())
            #print("fecha prueba2: ",datetime(2023, 7, 13, 10, 15, 00, 0).isocalendar())
            #print("fecha prueba3: ",datetime(2023, 7, 20, 10, 15, 00, 0).isocalendar())
            #print("fecha prueba4: ",datetime(2023, 7, 26, 10, 15, 00, 0).isocalendar())
            #print("fecha prueba4: ",datetime(2023, 7, 26, 10, 15, 00, 0).isocalendar()[1])

            #print("-----------------------------")

            #print("año: ",self.fecha_resultado.year)
            #print("mes: ",self.fecha_resultado.month)
            #print("dia: ",self.fecha_resultado.day)
            #print("hora: ",self.fecha_resultado.hour)
            #print("minuto: ",self.fecha_resultado.minute)
            #print("foto: ",self.fecha_resultado.second)
            #self.terminal = self.numero_foto.nombre
            print()

            print("-----------------------------")

            #Ingresando num de semana
            self.semana = datetime(self.fecha_resultado.year, self.fecha_resultado.month, self.fecha_resultado.day, 00, 00, 00, 0).isocalendar()[1]

            #lunes = 0
            #print("Numero del dia de la semana: ",(calendar.weekday(tiempo.year,tiempo.month,tiempo.day)))

            #dia de la semana
            #print(calendar.day_name[calendar.weekday(tiempo.year,tiempo.month,tiempo.day)])

        
            
            super(Resultados, self).save(*args, **kwargs)