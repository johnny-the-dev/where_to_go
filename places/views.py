from django.shortcuts import render
from django.templatetags.static import static

from .models import Place


# Create your views here.
def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coords.lng, place.coords.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeId,
                "detailsUrl": static(f'places/{place.placeId}.json'),  # TODO добавить рабочую ссылку
            }
        })
    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {'places_geojson': places_geojson}
    return render(request, 'places/index.html', context)
