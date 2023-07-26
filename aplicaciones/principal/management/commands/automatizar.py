from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.core.files.uploadedfile import UploadedFile

import os
import pathlib #esto es para contar la cantidad de archivos de un directorio

from datetime import time



#Aqui esta el modelo para crear dias de la semana
from aplicaciones.resultados.models import Dia


#Aqui esta el modelo para crear las horas
from aplicaciones.resultados.models import Hora

#Aqui esta el modelo para crear los signos
from aplicaciones.resultados.models import Signos

#Aqui esta el modelo para crear los animalitos
from aplicaciones.resultados.models import Animalitos

class Command(BaseCommand):
    help = 'comando para crear todo lo necesario'

    def handle(self, *args, **options):



        #Horas para jugar

        #hora1 = time(16,25,50)
        #print("hora: ",hora1)
        hora_11_00 = Hora.objects.create(hora=time(11,0,00))
        hora_12_00 = Hora.objects.create(hora=time(12,0,00))
        hora_01_00 = Hora.objects.create(hora=time(13,0,00))
        hora_04_00 = Hora.objects.create(hora=time(16,0,00))
        hora_07_00 = Hora.objects.create(hora=time(19,0,00))

        #Dias de la semana
        dia_lunes = Dia.objects.create(dia_semana="lunes",)
        dia_martes = Dia.objects.create(dia_semana="martes",)
        dia_miercoles = Dia.objects.create(dia_semana="miércoles",)
        dia_jueves = Dia.objects.create(dia_semana="jueves",)
        dia_viernes = Dia.objects.create(dia_semana="viernes",)
        dia_sábado = Dia.objects.create(dia_semana="sábado",)
        dia_domingo = Dia.objects.create(dia_semana="domingo",)

        

        

        
        
        #Signos a registrar#
        #Ruta donde esta el comando actual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir,"signos")
        #print(os.listdir(filepath))
        for path in os.listdir(filepath):

            if os.path.isfile(os.path.join(filepath, path)):

                #print(os.path.isfile(os.path.join(filepath, path)))

                #Nombre completo del archivo
                #print(os.path.split(os.path.join(filepath, path))[1])

                #Nombre sin la extension
                #print(os.path.splitext(os.path.split(os.path.join(filepath, path))[1])[0])

                #Comando para agregar todos los signos
                
                rutanueva = os.path.join(script_dir,"signos", str(os.path.split(os.path.join(filepath, path))[1]))
                signo = Signos(nombre=str(os.path.splitext(os.path.split(os.path.join(rutanueva, path))[1])[0]))
                f = open(rutanueva,"rb")
                #print(f)
                signo.imagen.save(str(os.path.split(os.path.join(rutanueva, path))[1]), File(f))
                
        

        #######################################################

        #Animales a registrar#
        #Ruta donde esta el comando actual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir,"animalitos")
        #print(os.listdir(filepath))
        for path in os.listdir(filepath):

            if os.path.isfile(os.path.join(filepath, path)):

                #print(os.path.isfile(os.path.join(filepath, path)))

                #Nombre completo del archivo
                #print(os.path.split(os.path.join(filepath, path))[1])

                #Nombre sin la extension
                #print(os.path.splitext(os.path.split(os.path.join(filepath, path))[1])[0])

                #Comando para agregar todos los signos
                
                rutanueva = os.path.join(script_dir,"animalitos", str(os.path.split(os.path.join(filepath, path))[1]))
                signo = Animalitos(nombre=str(os.path.splitext(os.path.split(os.path.join(rutanueva, path))[1])[0]))
                f = open(rutanueva,"rb")
                #print(f)
                signo.imagen.save(str(os.path.split(os.path.join(rutanueva, path))[1]), File(f))
        
        

                
        
        
        self.stdout.write(self.style.HTTP_SUCCESS("TODO CREADO CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))