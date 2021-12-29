from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Restaurant


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'address', 'rating')
    list_display = ('name', 'address', 'rating')


admin.site.register(Restaurant, AuthorAdmin)
