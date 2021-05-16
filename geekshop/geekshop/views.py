from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def main(request):
    products = Product.objects.all()[:4]

    context = {
        'slogan': 'Супер удобные стулья',
        'topic': 'Тренды',
        'products': products,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')
