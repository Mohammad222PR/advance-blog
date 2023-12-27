from django.shortcuts import render
import requests
from urllib.parse import quote
from .models import City
from .forms import CityForm

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=36424c65d4b47df6dc291259ca38682c"

    cities = City.objects.all()  # Return all the cities in the database
    form = CityForm()  # Initialize an empty form

    if request.method == 'POST':  # Only true if form is submitted
        form = CityForm(request.POST)  # Add actual request data to form for processing
        if form.is_valid():  # Check if the form is valid
            form.save()  # Validate and save if valid

    weather_data = []

    for city in cities:
        city_name = quote(city.name)  # URL encode city name
        city_weather = requests.get(url.format(city_name)).json()  # Use city name for API request

        weather = {
            'city': city_name,
            'temperature': city_weather.get('main', {}).get('temp'),
            'description': city_weather.get('weather', [{}])[0].get('description'),
            'icon': city_weather.get('weather', [{}])[0].get('icon')
        }

        weather_data.append(weather)  # Add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)  # Returns the index.html template
