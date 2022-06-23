
from django.urls import  path
from django.contrib import admin

from products.views import details, getProduct, indexP

urlpatterns = [
    path("list/",indexP,name='products'),
    path("details/",details,name='details')
    
]