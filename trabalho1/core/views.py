from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import ContatoForm

# Create your views here.
def index(request):
    matriculas = Matricula.objects.all()
    context = {
        'matriculas':matriculas
    }

    return render(request, 'index.html', context=context)

def verAluno(request, id):
    aluno = Matricula.objects.get(id=id)
    context = {
        'aluno':aluno
    }
    return render(request, 'aluno.html', context=context)

def contato(request):
    if request.method == 'POST':
        numero = request.POST.get('telefone')
        print(numero)
        form = ContatoForm(request.POST or None)
        context = {'form':form}
        if form.is_valid():
            form.send_mail()
            return redirect('index')
        else:
            print("EMIAL NAO ENVIADO")
    else:
        form = ContatoForm()
        context = {'form':form}
    return render(request, 'contato.html', context=context)