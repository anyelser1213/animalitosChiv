from django import template
from atexit import register

from aplicaciones.resultados.models import Dia
from aplicaciones.resultados.models import Resultados

register = template.Library()

@register.inclusion_tag('resultados/tr_consultas.html')
def obtener_resultados(semana,dia,hora):

    #print("Entramos en crear los TR")
    #print("semana: ", semana, "dia: ",dia," hora:",hora)
    dias_semana = Dia.objects.all()
    #print("Vantidad: ",Resultados.objects.filter(semana=semana,dia=dia,hora=hora).count())

    if Resultados.objects.filter(semana=semana,dia=dia,hora=hora).count()>0:
        resultado = Resultados.objects.get(semana=semana,dia=dia,hora=hora)
    else:
        resultado = None
    #Tipos = TipoJugadas.objects.filter(nombre=str(elemento))
    existen = False
    #print("Dia: ",dia," tipo:", type(dia))
    #print(" Hora:",hora," tipo: ",type(hora))
    archivos = [] #Creamos la lista



    #ruta = "videos/"+categoria_nombre+"/"+subcategoria_nombre
    return {
        'existe':existen,
        'resultado':resultado,
        #'ruta':"/media/"+categoria_nombre+"/"+subcategoria_nombre+"/"
    }



@register.simple_tag
def formateo_fecha(fecha):

    print("Probando aqui fecha inicial de la semana: ",fecha.replace('/','_'))


    #ruta = "videos/"+categoria_nombre+"/"+subcategoria_nombre
    return fecha.replace('/','_') 












