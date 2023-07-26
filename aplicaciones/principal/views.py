from django.shortcuts import redirect, render

import os

#Para las fechas
from datetime import datetime, time

#Funciones creadas
from aplicaciones.resultados.funciones import dia_mes_actual_consultas


#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView


from aplicaciones.resultados.models import Hora,Resultados


class Index(TemplateView):

    template_name = "principal/index2.html"
    #template_name = "principal/index.html"

    def dispatch(self, request, *args, **kwargs):



        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."

        #Esta funcion la creamos para traer fechas permitidas en django
        fecha_actual= dia_mes_actual_consultas()

        #print(prueba)

        horario_actual = datetime.now()
        print(horario_actual)

        #Horas
        hora_11_00 = Hora.objects.get(hora=time(11,0,00))
        hora_12_00 = Hora.objects.get(hora=time(12,0,00))
        hora_01_00 = Hora.objects.get(hora=time(13,0,00))
        hora_04_00 = Hora.objects.get(hora=time(16,0,00))
        hora_07_00 = Hora.objects.get(hora=time(19,0,00))

        
        if Resultados.objects.filter(fecha_resultado=fecha_actual).count()>0:
            context['resultadosUltimo'] = Resultados.objects.filter(fecha_resultado=fecha_actual).last() #Aqui haras un filtro por el dia de hoy
            context['resultadosGlobales'] = Resultados.objects.filter(fecha_resultado=fecha_actual).exclude(id=context['resultadosUltimo'].id) #Aqui haras un filtro por el dia de hoy
        else:
            context['resultadosUltimo'] = Resultados.objects.none()
            context['resultadosGlobales'] = Resultados.objects.none()

        print(context['resultadosGlobales'])
        #print("ultimo resultado: ",context['resultadosUltimo'])
        #print("ultimo resultado: ",context['resultadosUltimo'].id, " tipo: ",type(context['resultadosUltimo']))

        """
        context['resultado11am'] = None
        context['resultado12am'] = None
        context['resultado01am'] = None
        context['resultado04am'] = None
        context['resultado07am'] = None
        context['ultimoResultado'] = 0

        #Hacemos las consultas para los 5 resultados del dia de hoy:
        ultimoResultado = True

        #Resultado de las 11am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_11_00):
            context['resultado11am'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_11_00)
            context['ultimoResultado']  = 1
            
        else:
            context['resultado11am'] = None

        #Resultado de las 12am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_12_00):
            context['resultado12pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_12_00)
            context['ultimoResultado'] = 2
        else:
            context['resultado12pm'] = None

        #Resultado de las 01am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_01_00):
            context['resultado01pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_01_00)
            context['ultimoResultado'] = 3
        else:
            context['resultado01pm'] = None

        #Resultado de las 04am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_04_00):
            context['resultado04pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_04_00)
            context['ultimoResultado'] = 4
        else:
            context['resultado04pm'] = None

        #Resultado de las 07am
        if Resultados.objects.filter(fecha_resultado=fecha_actual,hora=hora_07_00):
            context['resultado07pm'] = Resultados.objects.get(fecha_resultado=fecha_actual,hora=hora_07_00)
            context['ultimoResultado'] = 5
        else:
            context['resultado07pm'] = None
        
        context['resultados'] = Resultados.objects.filter(fecha_resultado=fecha_actual) #Aqui haras un filtro por el dia de hoy

        print(context['resultados'])
        """
        
        return context

