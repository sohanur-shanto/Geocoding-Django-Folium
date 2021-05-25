from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Data, Search
import folium
from folium import plugins
from folium.plugins import MarkerCluster
import geocoder
from .forms import SearchForm
# Create your views here.


def index(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()

    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longtitude', 'population')
    
    #base_map
    map1 = folium.Map(location=[19, -12],
                      tiles='OpenStreetMap', zoom_start=2, control_scale=True, prefer_canvas=True)
    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)


    #circle for specific location
    folium.CircleMarker(
    location=[25.5850605, 89.6622435],
    radius=50,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(map1)


    #marker for specific location
    # folium.Marker(
    # location=[45.3300, -121.6823],
    # popup="Some Other Location",
    # icon=folium.Icon(color="green", icon="ok-sign"),).add_to(map1)


    

    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    if lat == None or lng == None:
        address.delete()
        return render(request, 'dashboard/error.html')

    folium.Marker([lat, lng], tooltip='click for more', popup= country).add_to(map1)





    # folium.raster_layer.TileLayer('Stamen Terrain').add_to(map1)
    # folium.raster_layer.TileLayer('Stamen Toner').add_to(map1)
    # folium.raster_layer.TileLayer('Stamen Watercolor').add_to(map1)
    # folium.raster_layer.TileLayer('CartoDB Positron').add_to(map1)

    # folium.LayerControl().add_to(map1)

    map1 = map1._repr_html_()
    context = {
        'map1': map1,
        'form' : form,
    }
    return render(request, 'dashboard/index.html', context)