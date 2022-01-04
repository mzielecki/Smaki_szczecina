from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Restaurant


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'address', 'district', 'price', 'rating')
    list_display = ('name', 'description', 'address', 'district', 'price', 'rating')


admin.site.register(Restaurant, AuthorAdmin)
