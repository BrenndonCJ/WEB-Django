from django.db import models

# Create your models here.
class Matricula(models.Model):

    choice_situacao = (
        ('A','Aprovado'),
        ('R','Reprovado'),
    )
    __tablename__ = 'matricula'
    nome = models.CharField("Nome", max_length=50)
    periodo = models.CharField("Periodo", max_length=7)
    disciplina = models.CharField("Disciplina", max_length=50)
    nota = models.DecimalField("Nota", decimal_places=1, max_digits=5)
    situacao = models.CharField("Situação", max_length=1, choices=choice_situacao)

    def __str__(self):
        return self.nome