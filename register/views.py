from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from .forms import UserRegist_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views

def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegist_form(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'user with this email already has been')
        else:
            if form.is_valid():
                ins= form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, email=email, password=password)
                ins.email = email
                ins.save()
                form.save_m2m()
                return redirect('/')
    else:
        form = UserRegist_form()
    info = {'info': form}
    return render(request, 'register/register.html', info)
