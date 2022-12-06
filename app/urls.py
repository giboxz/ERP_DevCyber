from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import editar_entrada, update_entrada, delete_entrada, editar_saida, update_saida, delete_saida, salva_excel_entradas, salva_excel_saidas

urlpatterns = [
    url(r'formEntrada/', views.form_entrada),
    url(r'consultaEntrada/', views.consulta_entrada),
    url(r'formSaida/', views.form_saida),
    url(r'consultaSaida/', views.consulta_saida),
    path("editarEntrada/<int:id>", editar_entrada, name='editar_entrada'),
    path("updateEntrada/<int:id>", update_entrada, name='update_entrada'),
    path("deleteEntrada/<int:id>", delete_entrada, name='delete_entrada'),
    path("editarSaida/<int:id>", editar_saida, name='editar_saida'),
    path("updateSaida/<int:id>", update_saida, name='update_saida'),
    path("deleteSaida/<int:id>", delete_saida, name='delete_saida'),
    path("salva_excel_entradas/", salva_excel_entradas, name='salva_excel_entradas'),
    path("salva_excel_saidas/", salva_excel_saidas, name='salva_excel_saidas')
] + static(settings.STATIC_URL)
