from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Restaurant, Categorie


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'category', 'address', 'district', 'price', 'rating', 'image')
    list_display = ('name', 'description', 'category', 'address', 'district', 'price', 'rating', 'image')


class AuthorAdmin2(admin.ModelAdmin):
    fields = ('category', )
    list_display = ('category', )


admin.site.register(Restaurant, AuthorAdmin)
admin.site.register(Categorie, AuthorAdmin2)
