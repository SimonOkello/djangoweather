from django.shortcuts import render
from . models import City

# Create your views here.

def index(request):
    cities = City.objects.all()
    return render(request, 'index.html', {'cities':cities})

