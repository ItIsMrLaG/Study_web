from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about123/', views.about, name='about'),
    path('info/', views.info, name='info'),
]