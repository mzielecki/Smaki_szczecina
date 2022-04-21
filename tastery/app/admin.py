from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Restaurant, Categorie, Opinions


class AuthorAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'description', 'category', 'address', 'district', 'price', 'rating', 'image', 'x', 'y')
    list_display = ('id', 'name', 'description', 'category', 'address', 'district', 'price', 'rating', 'image', 'x', 'y')


class AuthorAdmin2(admin.ModelAdmin):
    fields = ('category', )
    list_display = ('category', )

class AuthorAdmin3(admin.ModelAdmin):
    fields = ('id', 'restaurant_name', 'opinion', 'rating')
    list_display = ('id', 'restaurant_name', 'opinion', 'rating')


admin.site.register(Restaurant, AuthorAdmin)
admin.site.register(Categorie, AuthorAdmin2)
admin.site.register(Opinions, AuthorAdmin3)
