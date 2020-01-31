import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    """
    This is the initial route to our app
    """
    # Url below is an API from openweather website: http://api.openweathermap.org
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1be6324f259e2d5ad5e3f216c7627890'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()
# query all cities from the database
    cities = City.objects.all()

    weather_data = [] #list to hold the added cities

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        # Append the city weather to  data list
        weather_data.append(city_weather)

    return render(request, 'index.html', {'weather_data': weather_data, 'form': form})

# ROUTE TO DISPLAY THE CITIES ADDED BY THE USER
def citylist(request):
    if request.method == 'POST': #check if the form request is POST
        cityform = CityForm(request.POST)
        if cityform.is_valid():   #check if the form is valid
            cityform.save() #save the form data in the database

    cityform = CityForm()
    # query all the added cities from the database
    cities_list = City.objects.all()  
    return render(request, 'captured-cities.html', {'cities_list': cities_list, 'cityform':cityform})
