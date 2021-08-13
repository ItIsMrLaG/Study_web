from django.shortcuts import render, redirect
from .models import Information
from .forms import Informatin_form
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView


# ListView - class for comfortable output of all 'info' from bd
# DetailView - class for comfortable output of only one 'info' from bd
# UpdateView - class for updating information inside db
# DeleteView - class for deleting information from db


class Detail_output (DetailView):
    model = Information
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class News_update(UpdateView):
    model = Information
    template_name = 'news/create.html'
    form_class = Informatin_form


class News_delete(DeleteView):
    model = Information
    template_name = 'news/news-delete.html'
    success_url = '/news/'                        # url on place where people would be redirect before using this class

###################################################################################################################
'''
there are two same output-method for showing all information 
'''

class All_output (ListView):                      # method - 1
    model = Information
    template_name = 'news/for_check.html'
    context_object_name = 'all_art'               # key name, like {"news": news} in the second method


def news_home (request):                          # method - 2 (with sorting)
    # news = Information.objects.all()            # getting all information from the bd
    news = Information.objects.order_by('-date')  # sort get information by attribute
    news_dict = {"news": news}
    return render(request, 'news/news_home.html', news_dict)


##################################################################################################################

def create (request):
    error = ''
    if request.method == 'POST':
        form = Informatin_form(request.POST)
        if form.is_valid():                       # check (is this form was filled correct or not)
            form.save()                           # send info to the BD
            return redirect('home')               # direct you on the another page >>>redirect('name of this page')<<<
        else:
            error = 'Form with mistake'

    form = Informatin_form()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
