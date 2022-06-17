from django.shortcuts import redirect, render
from django.core.paginator import Page, Paginator, EmptyPage, PageNotAnInteger
from empresa.forms import ContactoForm
from .models import Foto
from django.db.models import Q
from datetime import datetime
#from __future__ import unicode_literals
# Create your views here.
def index(request):
    myDate = datetime.now()
    fotos = Foto.objects.all()
    return render(request, 'empresa/index.html', {'fotos':fotos, 'myDate': myDate})


def sobrenosotros(request):
    myDate = datetime.now()
    return render(request,  'empresa/sobre-nosotros.html', { 'myDate': myDate})


def servicios(request):
    myDate = datetime.now()
    fotos = Foto.objects.all()
    queryset = request.GET.get("buscar")
    fotos = Foto.objects.all()
    if  queryset:
        fotos = Foto.objects.filter(
            Q(name__icontains = queryset)            
        ).distinct()
    page = request.GET.get('page', 1)
    
    paginator = Paginator(fotos, 6)
    fotos = paginator.page(page)

    
    data1 = {
        'entity': fotos,
        'paginator': paginator
        }

    return render(request, 'empresa/servicios.html', {'fotos':fotos, 'entity': fotos, 'paginator': paginator, 'myDate': myDate})
  


def contacto(request):
    
    return render(request, 'empresa/contacto.html')    


def serviciospagina2(request):
    
    return render(request, 'empresa/serviciospagina2.html')    


def contactopass(request):
    
    return render(request, 'empresa/contactopass.html')        


def politicas(request):
    
    return render(request, 'empresa/politicas.html')      


def politicacookies(request):
    
    return render(request, 'empresa/politica-cookies.html')        





def contacto(request):

    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Enviado"
            return redirect('contactopass')
        else:
            data["form"] = formulario
                
    return render(request, 'empresa/contacto.html',  data)




