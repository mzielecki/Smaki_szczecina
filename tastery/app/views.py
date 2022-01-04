from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Restaurant, Categorie


def index(request: HttpRequest) -> HttpResponse:

    all_restaurants = Restaurant.objects.all()
    all_categories = Categorie.objects.all()
    return render(request, 'index.html', {
        'restaurants': all_restaurants,
        'categories': all_categories
    })


def restaurants(request: HttpRequest) -> HttpResponse:

    all_restaurants = Restaurant.objects.order_by()
    return render(request, 'restaurants.html', {
        'restaurants': all_restaurants
    })


def categories(request: HttpRequest) -> HttpResponse:

    all_categories = Categorie.objects.order_by()
    return render(request, 'restaurants.html', {
        'categories': all_categories
    })


def gallery(request: HttpRequest) -> HttpResponse:

    return render(request, 'gallery.html')


def about(request: HttpRequest) -> HttpResponse:

    return render(request, 'about.html')


def contacts(request: HttpRequest) -> HttpResponse:

    return render(request, 'contacts.html')





