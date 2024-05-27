from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    produtos = Produto.objects.all()

    teste = ''
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = f'Usuário logado: {request.user}'

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa',
        'usuario': teste,
        'produtos': produtos
    }
    return render(
        request=request,
        template_name='index.html',
        context=context
    )


def contato(request):
    print(request)
    return render(request=request,
                  template_name='contato.html')


def produto(request, produto_id):
    prod = get_object_or_404(Produto, pk=produto_id)
    context = {
        'produto': prod
    }
    return render(request=request,
                  template_name='produto.html',
                  context=context)


def error404(request, exception):
    template = loader.get_template('error_404.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=404
                        )


def error500(request): 
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500
                        )
