from pyexpat import model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()


class Supplier(models.Model):
    Company = models.CharField(max_length=50)
    adress = models.CharField( max_length=50)


