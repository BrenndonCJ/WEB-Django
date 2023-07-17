from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name='index'),
    path("cadastro/", view=views.cadastro, name='cadastro'),
    path("login/", view=views.logar, name='login'),
    path("logout/", view=views.sair, name='logout'),

    path("cadastroaluno/", view=views.cadastroaluno, name='cadastroaluno'),
]