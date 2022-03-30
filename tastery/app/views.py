from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Restaurant, Categorie


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def restaurants(request: HttpRequest) -> HttpResponse:
    all_categories = Categorie.objects.order_by()
    all_restaurants = Restaurant.objects.order_by('name')
    return render(request, 'restaurants.html', {
        'restaurants': all_restaurants,
        'categories': all_categories
    })


def gallery(request: HttpRequest) -> HttpResponse:
    return render(request, 'gallery.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, 'contacts.html')


def map(request: HttpRequest) -> HttpResponse:
    return render(request, 'map.html')


def restaurant(request: HttpRequest, res_id) -> HttpResponse:
    r = Restaurant.objects.get(id=res_id)
    context = {
        'restaurant': r
    }
    return render(request, 'sub_restaurant.html', context)