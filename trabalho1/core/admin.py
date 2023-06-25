from django.contrib import admin
from .models import Matricula


class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('nome','periodo','disciplina','nota','situacao')

# Register your models here.
admin.site.register(Matricula,MatriculaAdmin)