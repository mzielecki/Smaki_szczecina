from django.urls import path

from .views import index, contacts, restaurants, gallery

urlpatterns = [
    path('', index, name="index_page"),
    path('restaurants_list', restaurants, name="restaurants_list"),
    path('gallery', gallery, name="gallery"),
    path('contacts', contacts)
]
