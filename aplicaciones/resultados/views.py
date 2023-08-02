from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

import os

#Para las fechas
from datetime import datetime as SEM #para obtener las semanas
import datetime
import calendar
import locale





#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView
from aplicaciones.principal.BD_POSTGRES_DINAMICA.sqlite3 import todoSqlite3

from aplicaciones.resultados.funciones import informacionCalendario, calendarioPruebas,conversionValida, fecha_I_F,fecha_I_F_anterior,fecha_I_F_siguiente
from aplicaciones.resultados.models import Dia,Hora


class ListaResultados(TemplateView):

    template_name = "resultados/lista-resultados.html"

    def dispatch(self, request, *args, **kwargs):

        fecha_Actual = datetime.date.today()
        #print("Fecha actual: ",fecha_Actual)

        #numero_semana = fecha_Actual.isocalendar()
        #print("Numero de la semana actual: ",numero_semana[1])

        #Este locale es para cambiar el idioma al español
        locale.setlocale(locale.LC_ALL,"es_MX.UTF-8")

        #Esta funcion esta relacionada a las fechas en python
        informacionCalendario()

        #Para el calendario
        #calendarioPruebas()

        #dias de la semana
        print(list(calendar.day_name))


        #dias de los meses
        #print(list(calendar.month_name))
        #todoSqlite3()

        #informacionCalendario()


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."

        #Todas las variables que necesitamos
        #context['mes'] = "julio"

        #Asi obtenemos la semana actual
        context['semana'] = SEM.now().isocalendar()[1]
        #print("semana ingresada: ",context['semana'])
        context['semana_actual'] = True

        #Asi obtenemos la fecha inicial y final
        context['fecha_semana_inicial'], context['fecha_semana_final'] = fecha_I_F()
        #print("fecha: ",context['fecha_semana_inicial'])
        #print("fecha: ",type(context['fecha_semana_inicial']))
        context['horas'] = Hora.objects.all()
        context['dias'] = Dia.objects.all()

        return context




###### Para ver las listas anteriores y siguientes ########

def ListaResultadosAnteriores(request,fecha,semana):
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("fecha ingresada:",fecha)
            print("semana ingresada:",semana)


            semana_actual = SEM.now().isocalendar()[1]
            semana = semana-1
            print("semana modificada:",semana)
            print("semana actual:",semana_actual)
            
            if semana_actual == semana:
                 semana_actual = True
            else:
                 semana_actual = False

            print("semana: ",semana_actual)

            fecha_semana_inicial,fecha_semana_final = fecha_I_F_anterior(conversionValida(fecha))

            #Colocamos aqui todas las variables de contexto
            contexto = {'semana':semana,'semana_actual':semana_actual,'fecha_semana_inicial':str(fecha_semana_inicial),'fecha_semana_final':str(fecha_semana_final),'horas':Hora.objects.all(),'dias':Dia.objects.all()}
        
        return render(request, 'resultados/lista-resultados.html',contexto)




def ListaResultadosSiguientes(request,fecha,semana):
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("fecha ingresada:",fecha)
            print("semana ingresada:",semana)


            semana_actual = SEM.now().isocalendar()[1]
            semana = semana+1
            print("semana modificada:",semana)
            print("semana actual:",semana_actual)

            if semana_actual == semana:
                 semana_actual = True
            else:
                 semana_actual = False


            fecha_semana_inicial,fecha_semana_final = fecha_I_F_siguiente(conversionValida(fecha))

            #Colocamos aqui todas las variables de contexto
            contexto = {'semana':semana,'semana_actual':semana_actual,'fecha_semana_inicial':str(fecha_semana_inicial),'fecha_semana_final':str(fecha_semana_final),'horas':Hora.objects.all(),'dias':Dia.objects.all()}
        
        return render(request, 'resultados/lista-resultados.html',contexto)

