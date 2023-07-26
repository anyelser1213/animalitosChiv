from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ="resultados"

urlpatterns = [
    #path('', views.Index.as_view(), name='index'),
    
    path('listaResultados/', views.ListaResultados.as_view() ,name="listaResultados"),
    path('semana anterior/<slug:fecha>/<int:semana>/', views.ListaResultadosAnteriores ,name="SemanaAnterior"),
    path('semana siguiente/<slug:fecha>/<int:semana>/', views.ListaResultadosSiguientes ,name="SemanaSiguiente"),


    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)