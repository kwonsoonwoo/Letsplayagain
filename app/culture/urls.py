from django.urls import path

app_name = 'culture'

from . import views

urlpatterns = [
    path('', views.culture_list, name='culture-list'),
    path('<int:pk>/', views.culture_detail, name='culture-detail'),
]
