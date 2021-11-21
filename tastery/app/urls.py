from django.urls import path

from .views import index, contacts, restaurants

urlpatterns = [
    path('', index, name="index_page"),
    path('restaurants_list', restaurants, name="restaurants_list"),
    path('contacts', contacts)
]
