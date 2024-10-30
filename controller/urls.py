from django.contrib import admin
from django.urls import path, include
from agendamento import views

urlpatterns = [
    path('admin/', admin.site.urls), #Rota de admin
    path('', views.home, name="home"), #Rota da homepage
    path('agendamento/', include('agendamento.urls')), #Rota de redirecionamento
    path('accounts/', include('django.contrib.auth.urls')), #Rota de login
]