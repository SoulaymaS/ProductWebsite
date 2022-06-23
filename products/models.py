from pyexpat import model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    url= models.URLField(default="")
    def __str__(self):
        return self.name


class Supplier(models.Model):
    company = models.CharField(max_length=50)
    adress = models.CharField( max_length=50)
    Product = models.ForeignKey('Product', on_delete=models.PROTECT,default=0)
    def __str__(self):
        return self.company

