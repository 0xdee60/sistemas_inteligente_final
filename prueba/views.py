from django.shortcuts import redirect, render
from .models import Prueba
from .forms import PruebaForm
from django.core.files.base import ContentFile, File
def home_prueba(request):
    contexto = {}
    return render(request, 'home.html', contexto)


def realizar_prueba(request):
    if(request.method == "POST"):
        form = PruebaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_prueba')
    
    else:
        pass

    contexto = {}
    return render(request,'realizar_prueba.html',contexto)
