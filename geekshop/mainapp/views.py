from django.shortcuts import render


def products(request):
    links_menu = {
        'links': [
            {'href': 'mainapp:products', 'name': 'все'},
            {'href': 'mainapp:products', 'name': 'дом'},
            {'href': 'mainapp:products', 'name': 'офис'},
            {'href': 'mainapp:products', 'name': 'модерн'},
            {'href': 'mainapp:products', 'name': 'классика'},
        ]
    }
    return render(request, 'products.html', context=links_menu)
