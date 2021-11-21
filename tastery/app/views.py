from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:

    return render(request, 'index.html')


def restaurants(request: HttpRequest) -> HttpResponse:

    return render(request, 'restaurants.html')


def contacts(request: HttpRequest) -> HttpResponse:

    return render(request, 'contacts.html')





