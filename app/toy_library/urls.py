from django.urls import path

from . import views

app_name = 'toy-library'
urlpatterns = [
    path('', views.index, name='index'),
]