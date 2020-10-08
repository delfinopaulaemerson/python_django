from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

#criando a view index.html
#depois devera criar as rotas no arquivo de url
def index(request):

    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'outro':'Django é massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

#criando a view contato.html
#depois devera criar as rotas no arquivo de url
def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #recupera o objeto por id
    #p = Produto.objects.get(id=pk)
    p = get_object_or_404(Produto, id=pk)

    context ={
        'produto':p
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html charset=utf8', status=500)