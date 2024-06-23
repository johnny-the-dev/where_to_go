from django.urls import include, path

from places import views

urlpatterns = [
    path('', views.index),
    path('tinymce/', include('tinymce.urls')),
    path('places/<slug:place_id>/', views.place_detail_view, name='place_detail'),
]
