from django.shortcuts import render


def main(request):
    context = {
        'slogan': 'Супер удобные стулья',
        'topic': 'Тренды'
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')
