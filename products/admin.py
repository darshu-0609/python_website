from django.contrib import admin

from .models import Products

from .models import Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(Products,ProductAdmin)

class offersAdmin(admin.ModelAdmin):
    list_display = ("discount_code","discount_value")
admin.site.register(Offer,offersAdmin)
