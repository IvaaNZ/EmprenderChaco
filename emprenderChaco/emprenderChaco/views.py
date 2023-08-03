from django.shortcuts import render
from apps.noticias.models import Noticia

def index(request):
    noticias = Noticia.objects.order_by('-creado')[:3]
    return render(request, 'index.html', {'noticias': noticias})



#def index(request):
 #   return render(request, 'index.html', {'is_index': True})

def nosotros(request):
    return render(request, 'nosotros/nosotros.html')
