from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
