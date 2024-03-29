from django.db import models

# Create your models here.
class Categorie(models.Model):
    category = models.CharField(max_length=50)

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=True, null=False)
    x = models.CharField(max_length=100)
    y = models.CharField(max_length=100)

class Opinions(models.Model):
    id = models.IntegerField(primary_key=True)
    restaurant_name = models.CharField(max_length=50)
    opinion = models.CharField(max_length=1000)
    rating = models.CharField(max_length=30)
