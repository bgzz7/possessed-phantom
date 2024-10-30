from django.urls import path
from . import views

urlpatterns = [
#NOMEDOSITE.com - homepage
#NOMEDOSITE.com/agendamento - agendar

    path('', views.agendar, name='agendar'), #URL vazia
    path('sucesso/', views.sucesso, name='sucesso'),
]