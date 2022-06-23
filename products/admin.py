from django.contrib import admin

from products.models import Product, Supplier

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Supplier)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price")
    
    
@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display=("company",)