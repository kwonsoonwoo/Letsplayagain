from django.urls import path

from . import views

app_name = 'kidscafe'
urlpatterns = [
    path('', views.index, name='index')
]