from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {
        'curso' : 'Programação Web com Django Framework, página Index!',
    }

    return render(request, 'index.html', context)

def contato(request):
    context = {
        'cursonocontato' : 'Programação Web com Django Framework, página de contato!',
    }
    return render(request, 'contato.html', context)
