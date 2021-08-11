from django.shortcuts import render, redirect
from .models import Information
from .forms import Informatin_form


def news_home (request):
    # news = Information.objects.all()            # getting all information from the bd
    news = Information.objects.order_by('-date')  # sort get information by attribute
    news_dict = {"news": news}
    return render(request, 'news/news_home.html', news_dict)


def create (request):
    error = ''
    if request.method == 'POST':
        form = Informatin_form(request.POST)
        if form.is_valid():          # check (is this form was filled correct or not)
            form.save()              # send info to the BD
            return redirect('home')  # direct you on the another page >>>redirect('name of this page')<<<
        else:
            error = 'Form with mistake'

    form = Informatin_form()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
