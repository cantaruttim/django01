from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):

    produtos = Produto.objects.all()

    context = {
        # podemos acessar esse valor utilizando no .html {{ curso }}
        'curso': 'Programação Web com Django Framework',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    # print(f'Produto com id = {id}')
    #prod = Produto.objects.get(id=id)

    # podemos redirecionar o nosso cliente para uma pagina não encontrada e não mostrar erro
    prod = get_object_or_404(Produto, id=id)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    """Nome da View, deve ser a mesma informada em django01.urls.py"""
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500)