from django.urls import path

from .views import index, contacts, restaurants, gallery, about, map, restaurant, opinions

urlpatterns = [
    path('', index, name="index_page"),
    path('restaurants_list', restaurants, name="restaurants_list"),
    path('among us', about, name="about_page"),
    path('gallery', gallery, name="gallery"),
    path('map', map, name="map"),
    path('opinions', opinions, name="opinions"),
    path('restaurant/<str:res_id>', restaurant, name="restaurant"),
    path('contacts', contacts)
]
