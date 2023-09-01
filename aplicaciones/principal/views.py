from django.shortcuts import redirect, render

import os

#Para las fechas
from datetime import datetime, time
import calendar
import locale

#Funciones creadas
from aplicaciones.resultados.funciones import dia_mes_actual_consultas


#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView


from aplicaciones.resultados.models import Dia,Hora,Resultados


class Index(TemplateView):

    template_name = "principal/index.html"
    #template_name = "principal/index.html"

    def dispatch(self, request, *args, **kwargs):



        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."

        #Esta funcion la creamos para traer fechas permitidas en django
        fecha_actual= dia_mes_actual_consultas()


        #Este locale es para cambiar el idioma al español
        locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")

        horario_actual = datetime.now()
        print("dia semana: ",horario_actual.weekday())

        print("Calendario de Marzo 2023")
        #print(calendar.month(tiempo.year,tiempo.month))


        print("Calendario de la semana 2023")

        #numero_semana = horario_actual.isocalendar()
        #print("Todo: ",numero_semana)
        #print("Numero de la semana actual: ",numero_semana[1])
        #lunes = 0
        #print("Numero del dia de la semana: ",(calendar.weekday(horario_actual.year,horario_actual.month,horario_actual.day)))

        #dia de la semana
        dia_Actual = calendar.day_name[calendar.weekday(horario_actual.year,horario_actual.month,horario_actual.day)]
        print(dia_Actual)
        
        #objeto del dia
        dia_objeto = Dia.objects.get(dia_semana=dia_Actual)
        #print(dia_objeto)

        #Horas
        hora_11_00 = Hora.objects.get(hora=time(11,0,00))
        hora_12_00 = Hora.objects.get(hora=time(12,0,00))
        hora_01_00 = Hora.objects.get(hora=time(13,0,00))
        hora_04_00 = Hora.objects.get(hora=time(16,0,00))
        hora_07_00 = Hora.objects.get(hora=time(19,0,00))

        
        context['resultado11am'] = None
        context['resultado12pm'] = None
        context['resultado01pm'] = None
        context['resultado04pm'] = None
        context['resultado07pm'] = None
        context['resultadoEspecial'] = None
    

        #Hacemos las consultas para los 5 resultados del dia de hoy:
        ultimoResultado = True

        #Resultado de las 11am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_11_00,dia=dia_objeto.id):
            context['resultado11am'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_11_00,dia=dia_objeto.id)
            
        else:
            context['resultado11am'] = None

        #Resultado de las 12am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_12_00,dia=dia_objeto.id):
            context['resultado12pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_12_00,dia=dia_objeto.id)
        
        else:
            context['resultado12pm'] = None

        #Resultado de las 01am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_01_00,dia=dia_objeto.id):
            context['resultado01pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_01_00,dia=dia_objeto.id)
        
        else:
            context['resultado01pm'] = None

        #Resultado de las 04am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_04_00,dia=dia_objeto.id):
            context['resultado04pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_04_00,dia=dia_objeto.id)
        
        else:
            context['resultado04pm'] = None

        #Resultado de las 07am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_07_00,dia=dia_objeto.id):
            context['resultado07pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_07_00,dia=dia_objeto.id)
        
        else:
            context['resultado07pm'] = None
        
        #context['resultados'] = Resultados.objects.filter(fecha_resultado=fecha_actual) #Aqui haras un filtro por el dia de hoy

        #print(context['resultados'])
        
        return context

