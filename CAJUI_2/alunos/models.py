from django.db import models
from stdimage.models import StdImageField

# Create your models here.
class Base(models.Model):

    criado = models.DateField('Data de Criação',auto_now_add=True)
    modificado = models.DateField('Data de Atualização',auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Aluno(Base):

    __tablename__ = 'aluno'
    imagem = StdImageField('Imagem', upload_to='alunos',variations={'thumb': (124,124)})
    nome = models.CharField("Nome", max_length=50)
    cpf = models.CharField("cpf", max_length=11, unique=True)
    rg = models.CharField("RG", max_length=50)
    idade = models.IntegerField("Idade")
    curso = models.CharField("Curso", max_length=50)
    datanascimento = models.DateField("Data de nascimento", auto_now=False, auto_now_add=False)
    dataingresso = models.DateField("Data de ingresso", auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.nome