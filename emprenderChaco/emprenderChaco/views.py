from django.shortcuts import render




def index(request):
    return render(request, 'index.html', {'is_index': True})

def nosotros(request):
    return render(request, 'nosotros/nosotros.html')
