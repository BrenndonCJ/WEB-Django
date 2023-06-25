from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

# Create your views here.
def index(requests):
    return render(requests,"index.html")

def w3c(requests):
    return render(requests,"w3c.html")

def html(requests):
    return render(requests,"html.html")

def css(requests):
    return render(requests,"css.html")

def javascript(requests):
    return render(requests,"javascript.html")

def contato(requests):
    form = ContatoForm(requests.POST or None)
    context = {'form':form}
    if requests.method == 'POST':

        if form.is_valid():
            form.send_mail()
        else:
            print("Email nao enviado")
        return redirect('index')
    return render(requests,"faleconosco.html", context)