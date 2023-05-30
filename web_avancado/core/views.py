from django.shortcuts import render, redirect

# Create your views here.
def index(requests):
    return render(requests,"index.html")

def html(requests):
    return render(requests,"html.html")

def w3c(requests):
    return render(requests,"w3c.html")