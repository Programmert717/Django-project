from django.shortcuts import render

from products.models import Product, Category


def index(request):
    context = {
        'title': 'Store',
        'is_promotion': True
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
    }

    return render(request, 'products/products.html', context)
