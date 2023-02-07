from django.contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/one/', views.view_list, name='view_list'),
]
