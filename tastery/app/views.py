from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Restaurant, Categorie, Opinions


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def restaurants(request: HttpRequest) -> HttpResponse:

    category = request.GET.get('category')

    if category == None or category == 'Wszystkie':
        restaurants = Restaurant.objects.order_by('name')
    else:
        restaurants = Restaurant.objects.filter(category__category=category)

    categories = Categorie.objects.all()

    return render(request, 'restaurants.html', {
        'restaurants': restaurants,
        'categories': categories
    })


def gallery(request: HttpRequest) -> HttpResponse:
    return render(request, 'gallery.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def opinions(request: HttpRequest) -> HttpResponse:
    return render(request, 'opinions.html')


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

def opinions(request: HttpRequest) -> HttpResponse:
    opinions = Opinions.objects.order_by('id')
    return render(request, 'opinions.html', {
        'opinions': opinions
    }
    )
