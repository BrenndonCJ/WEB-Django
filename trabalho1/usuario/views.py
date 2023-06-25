from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# FURURA SESSÃO DE USUARIOS.
@login_required
def logar(request):
    return HttpResponse("logado")

@login_required
def cadastro(request):
    return HttpResponse("cadastrar")

@login_required
def sair(request):
    return HttpResponse("logout")