from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .mydecorators import anonymous_required

from django.contrib.auth.models import User
from .models import Aluno

# Sessão neutra
def index(request):
    if request.user.is_authenticated:
        alunos = Aluno.objects.all()
        context = {
            'alunos':alunos
        }
        return render(request, "alunos/lista.html", context=context)
    return render(request, "alunos/login.html")

# Sessões de gerenciamento
def cadastroaluno(request):
    if request.method == "POST":
        foto = request.FILES.get("foto")
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg")
        data_nascimento = request.POST.get("datanascimento")
        data_ingresso = request.POST.get("ingressoinstituicao")
        curso = request.POST.get("curso")

        aluno = Aluno(
            imagem=foto,
            nome=nome,
            cpf=cpf,
            rg=rg,
            idade=idade,
            curso=curso,
            datanascimento=data_nascimento,
            dataingresso=data_ingresso,
        )
        aluno.save()

        return redirect('index')
    return render(request, 'alunos/cadastro_aluno.html')

# Sessões de usuarios
# cadastro
@anonymous_required
def cadastro(request):

    if request.method == "POST":
        username = request.POST.get("nome")
        password = request.POST.get("senha")
        if (username and password) and (len(str(username)) > 0 and len(str(password)) > 0):
            
            user = User.objects.create_user(
                username = username,
                password = password
            )
        else:
            return HttpResponse("Preencha os campos corretamente")
        return redirect("login")
    
    return render(request, 'alunos/cadastro.html')

# login
@anonymous_required
def logar(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)

        user = authenticate(
            username= username,
            password= password,
        )

        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    
    return render(request, "alunos/login.html")

# logout
@login_required
def sair(request):
    logout(request)
    return redirect('login')