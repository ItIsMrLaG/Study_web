from django.shortcuts import render
from .models import Information

def news_home (request):
    # news = Information.objects.all()            # getting all information from the bd
    news = Information.objects.order_by('-date')  # sort get information by attribute
    news_dict = {"news": news}
    return render(request, 'news/news_home.html', news_dict)
