from django.urls import path

from . import views

app_name = 'park'
urlpatterns = [
    path('', views.park_list, name='park-list'),
    path('<int:pk>/', views.park_detail, name='park-detail'),
]