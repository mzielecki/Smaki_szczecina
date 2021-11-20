from django.urls import path

from .views import index, contacts


urlpatterns = [
    path('', index, name="index_page"),
    path('contacts', contacts)
]
