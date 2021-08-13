from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.Detail_output.as_view(), name='news_detail'),  # <int:pk> - it is dynamical url (means - a parameter is supplied to it, which must be an int)
    path('checker', views.All_output.as_view(), name='check'),
]