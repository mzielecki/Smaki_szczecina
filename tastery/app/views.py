from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Restaurant


def index(request: HttpRequest) -> HttpResponse:

    all_restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {
        'restaurants': all_restaurants
    })


def restaurants(request: HttpRequest) -> HttpResponse:

    all_restaurants = Restaurant.objects.order_by()
    return render(request, 'restaurants.html', {
        'restaurants': all_restaurants
    })


def gallery(request: HttpRequest) -> HttpResponse:

    return render(request, 'gallery.html')


def contacts(request: HttpRequest) -> HttpResponse:

    return render(request, 'contacts.html')





