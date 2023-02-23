from django.contrib import admin
from django.urls import path, include
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    path('', list_views.home_page, name='home'),
    path('lists/', include(list_urls))
    ]
"""path('lists/new', views.new_list, name='new_list'),
    path('lists/<list_id>/', views.view_list, name='view_list'),
    path('lists/<list_id>/add_item', views.add_item, name='add_item'),
"""