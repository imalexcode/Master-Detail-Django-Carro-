from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Carro

def index(request):
    carros = Carro.objects.all()
    return render(request, 'index.html', {'carros': carros})

def detalhe(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    return render(request, 'detalhes.html', {'carro': carro})

