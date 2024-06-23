from django.urls import path

from places import views

urlpatterns = [
    path('', views.index),
    path('places/<slug:place_id>/', views.place_detail_view, name='place_detail'),
]
