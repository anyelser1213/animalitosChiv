from django.urls import path
from aplicaciones.principal.api.api import consultarPermisos_api_view


urlpatterns = [

    #Normal

    #APIS PARA LA APP MOVIL
    path('consultarpermisos/',consultarPermisos_api_view,name='consultar_permisos_usuarios'),
    
]