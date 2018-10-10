from django.urls import path

from . import views

app_name = 'toylibrary'
urlpatterns = [
    path('', views.toylibrary_list, name='toylibrary-list'),
]