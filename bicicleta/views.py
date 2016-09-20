from django.shortcuts import render
from .models import Bicicleta

def bike_list(request):
    bicicleta = Bicicleta.objects.filter(fabricante__contains='')
    return render(request, 'bicicleta/bike_list.html', {'bicicleta':bicicleta})
# Create your views here.
