
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

from django.shortcuts import render, redirect

from .forms import MyLoginForm

def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            from django.contrib.auth import login
            user = form.get_user()
            login(request, user)
            return redirect('nombre_de_la_url_de_inicio')  # Reemplaza 'nombre_de_la_url_de_inicio' con la URL a la que deseas redirigir al usuario después de iniciar sesión correctamente.
    else:
        form = MyLoginForm()
    
    return render(request, 'login.html', {'form': form})



class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'