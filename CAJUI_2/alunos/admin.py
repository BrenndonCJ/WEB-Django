from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'modificado', 'ativo')