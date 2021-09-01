from django.urls import path
from . import views


urlpatterns = [
    path('', views.param_reader, name='home_js'),
    path('myJson/', views.json_sender, name='config'),
]