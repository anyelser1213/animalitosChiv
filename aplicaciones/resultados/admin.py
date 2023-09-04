from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from aplicaciones.resultados.models import *

# Register your models here.


admin.site.register(Hora)
admin.site.register(Animalitos)
admin.site.register(Signos)
admin.site.register(Numeros)



class DiaAdmin(admin.ModelAdmin):
    
    ordering = ('digito_dia_semana',)
    
    #Aqui es cuando se va a editar
    """
    fieldsets = (
        #Aqui es para editar
        ("Informacion Esencial", {'fields': ('dia_semana')}),
        
    )
    """

    #Aqui es cuando se esta creando
    add_fieldsets = (
        ("Registro", {
            'classes': ('wide',),
            'fields': ('dia_semana',),
        }),
    )
    fields = ('dia_semana',)


    #Para indicarle al admin que campos queremos mostrar
    list_display = ('dia_semana','digito_dia_semana')
    #list_display = ('username', 'email','is_superuser','admin','rol','plan_elegido')
    list_filter = ('dia_semana',)
    
    #Para especificar que campos van a efectuar la busqueda
    search_fields = ('dia_semana',)
    filter_horizontal = ()

class ResultadosAdmin(admin.ModelAdmin):
    
    ordering = ('sorteo',)
    
    #Aqui es cuando se va a editar
    fieldsets = (
        #Aqui es para editar
        ("Informacion Esencial", {'fields': ('sorteo','dia','hora','animalito','numero_foto','signo','fecha_resultado')}),
        
    )

    #Aqui es cuando se esta creando
    add_fieldsets = (
        ("Registro", {
            'classes': ('wide',),
            'fields': ('semana','dia','hora','animalito','numero_foto','signo','fecha_resultado'),
        }),
    )


    #Para indicarle al admin que campos queremos mostrar
    list_display = ('id','sorteo','semana','dia','hora','animalito','terminal','numero_foto','signo','fecha_resultado')
    
    #list_display = ('username', 'email','is_superuser','admin','rol','plan_elegido')
    list_filter = ('sorteo','dia','hora','animalito','terminal','numero_foto','signo','fecha_resultado')
    
    #Para especificar que campos van a efectuar la busqueda
    search_fields = ('sorteo','hora','dia','animalito','terminal','numero_foto','signo','fecha_resultado')
    filter_horizontal = ()







#Aqui registramos los elementos para que aparezcan en el admin de django
admin.site.register(Dia,DiaAdmin)
admin.site.register(Resultados,ResultadosAdmin)



#admin.site.register(Resultados)
