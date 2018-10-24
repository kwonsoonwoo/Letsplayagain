from django.urls import path

from . import views

app_name = 'kidscafe'
urlpatterns = [
    path('', views.kidscafe_list, name='kidscafe-list'),
    path('<int:pk>/', views.kidscafe_detail, name='kidscafe-detail'),
]