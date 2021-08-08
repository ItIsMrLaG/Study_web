from django.shortcuts import render
# Create your views here.

def index(request):
    info = {
        'title': "index.html(переданные изнаутри параметры)",
        'values': ['Yo', 'Hello', 'Mr.LaG'],
        'objects': {
            'number': 99,
            'info': 'как вытащить значение из многомерного массива',
        }
    }
    return render(request, 'main/index.html', info)


def about(request):
    info = {
        'title': "index.html(переданные изнаутри параметры)",
        'values': ['It', 'Is', 'Mr.LaG'],
        'objects': {
            'number': "eighty",
            'info': 'как вытащить значение из многомерного массива версия2',
        }
    }
    return render(request, 'main/about.html', info)
