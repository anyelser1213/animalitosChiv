from django import template
from atexit import register

from aplicaciones.resultados.models import *

register = template.Library()



@register.simple_tag
def ceros_en_sorteo(valor): # Only one argument.
    
    
    #print("El tipo insertado es: ",tipo)
    numero = int(valor)
    if numero > 1000:
        return numero
    elif numero >100 and numero < 1000:
        return "0"+str(numero)
    elif numero > 10 and numero < 100:
        return "00"+str(numero)
    else:
        return "000"+str(numero)
    





