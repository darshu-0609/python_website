from django.contrib import admin

from .models import Product,Category

from .models import Offer

class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name")

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','category')

class offersAdmin(admin.ModelAdmin):
    list_display = ("discount_code","discount_value")

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,offersAdmin)
admin.site.register(Category,CategoryAdmin)

