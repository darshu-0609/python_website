from collections import defaultdict
from django.http import HttpResponse
from .models import Product,Category
from django.shortcuts import render

def index(request):
    products = Product.objects.select_related('category').all()  # Get all products
    grouped_product = defaultdict(list)
    for product in products:
        grouped_product[product.category.name].append(product)

    # Sort categories alphabetically
    sorted_grouped_product = dict(sorted(grouped_product.items()))

    context = {
        'grouped_product': sorted_grouped_product  # Pass sorted grouped data
    }
    return render(request, 'index.html', context)

def new(request):
    return HttpResponse("New Products")

def product_list(request):
    categories = Category.objects.prefetch_related('products').all()
    context = {
        'categories': categories
    }
    return render(request, 'your_template.html', context)