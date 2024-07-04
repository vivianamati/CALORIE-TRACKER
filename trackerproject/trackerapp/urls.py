# tracker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('add/', views.add_food, name='add_food'),
    path('remove/<int:food_id>/', views.remove_food, name='remove_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
]
