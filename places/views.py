from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
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


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, placeId=place_id)
    imgs_urls = list(place.images.all().values_list('image', flat=True))
    coordinates = {
        'lat': place.coords.lat,
        'lng': place.coords.lng
    }
    return JsonResponse(
        {
            'title': place.title_full,
            'imgs': imgs_urls,
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': coordinates
        },
        json_dumps_params={'indent': 2, 'ensure_ascii': False}
    )
