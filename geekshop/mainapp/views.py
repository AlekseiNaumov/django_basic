from django.shortcuts import render
from .models import ProductCategory


def products(request):
    categories = ProductCategory.objects.all()
    links_name = []
    for category in categories:
        category = {'href': 'mainapp:products', 'name': category.name}
        links_name.append(category)

    links_menu = {'links': links_name}

    return render(request, 'products.html', context=links_menu)
